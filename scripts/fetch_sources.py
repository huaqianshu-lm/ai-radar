from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import feedparser
import httpx
import trafilatura
import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCES_PATH = ROOT / "config" / "sources.yaml"
ENV_LOCAL_PATH = ROOT / ".env.local"
RAW_DIR = ROOT / "data" / "raw"
LOG_PATH = ROOT / "logs" / "run.log"


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def slugify(value: str, max_length: int = 80) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        slug = hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]
    return slug[:max_length].strip("-")


def yaml_scalar(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace('"', '\\"')


def write_log(message: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = utc_now().isoformat()
    with LOG_PATH.open("a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def load_sources() -> list[dict[str, Any]]:
    with SOURCES_PATH.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    return [source for source in data.get("sources", []) if source.get("enabled")]


def env_local_values() -> dict[str, str]:
    if not ENV_LOCAL_PATH.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in ENV_LOCAL_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        values[key] = value
    return values


def secret_value(name: str) -> str:
    value = os.environ.get(name)
    if value:
        return value
    return env_local_values().get(name, "")


def parse_date(value: str | None) -> str:
    if not value:
        return ""
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return value
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def entry_to_raw(source: dict[str, Any], entry: Any, fetched_at: str) -> dict[str, str]:
    title = str(entry.get("title", "")).strip() or "Untitled"
    url = str(entry.get("link", source.get("url", ""))).strip()
    summary = str(entry.get("summary", "") or entry.get("description", "")).strip()
    published_at = parse_date(entry.get("published") or entry.get("updated"))

    soup = BeautifulSoup(summary, "html.parser")
    text = soup.get_text("\n", strip=True) if summary else ""

    return {
        "title": title,
        "url": url,
        "source": str(source.get("name", "")),
        "source_type": str(source.get("type", "")),
        "published_at": published_at,
        "fetched_at": fetched_at,
        "content_type": "markdown",
        "is_list_page": "false",
        "content": text or summary or url,
    }


def fetch_rss(source: dict[str, Any], limit: int, fetched_at: str) -> list[dict[str, str]]:
    try:
        feed = feedparser.parse(fetch_text(source["url"]))
    except Exception as error:
        write_log(f"rss fetch_text failed, fallback to feedparser: {source['name']}: {error}")
        feed = feedparser.parse(source["url"])

    if getattr(feed, "bozo", False):
        write_log(f"rss parse warning: {source['name']}: {getattr(feed, 'bozo_exception', '')}")
    if not feed.entries:
        raise RuntimeError("RSS returned 0 entries")
    return [entry_to_raw(source, entry, fetched_at) for entry in feed.entries[:limit]]


def fetch_text(url: str) -> str:
    try:
        with httpx.Client(timeout=20.0, follow_redirects=True) as client:
            response = client.get(url, headers={"User-Agent": "ai-radar/0.1"})
            response.raise_for_status()
        return response.text
    except Exception as error:
        write_log(f"httpx failed, fallback to curl: {url}: {error}")
        result = subprocess.run(
            [
                "curl",
                "-L",
                "--fail",
                "--silent",
                "--show-error",
                "--max-time",
                "60",
                "--compressed",
                url,
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=70,
        )
        return result.stdout


def html_to_raw_item(source: dict[str, Any], url: str, html: str, fetched_at: str, is_list_page: bool) -> dict[str, str]:
    extracted = trafilatura.extract(html, url=url, output_format="markdown")
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(strip=True) if soup.title else source.get("name", "Untitled")

    return {
        "title": title,
        "url": url,
        "source": str(source.get("name", "")),
        "source_type": str(source.get("type", "")),
        "published_at": "",
        "fetched_at": fetched_at,
        "content_type": "markdown",
        "is_list_page": "true" if is_list_page else "false",
        "content": extracted or soup.get_text("\n", strip=True)[:5000],
    }


def article_links(source: dict[str, Any], html: str, limit: int) -> list[str]:
    source_url = str(source["url"])
    parsed_source = urlparse(source_url)
    source_path = parsed_source.path.rstrip("/")
    article_path_prefix = str(source.get("article_path_prefix") or source_path + "/")
    soup = BeautifulSoup(html, "html.parser")
    links: list[str] = []
    seen: set[str] = set()

    for anchor in soup.find_all("a", href=True):
        url = urljoin(source_url, anchor["href"])
        parsed = urlparse(url)
        if parsed.netloc != parsed_source.netloc:
            continue
        path = parsed.path.rstrip("/")
        if not path.startswith(article_path_prefix.rstrip("/")):
            continue
        if path == source_path:
            continue
        if path.count("/") <= article_path_prefix.rstrip("/").count("/"):
            continue
        clean_url = f"{parsed.scheme}://{parsed.netloc}{path}"
        if clean_url in seen:
            continue
        seen.add(clean_url)
        links.append(clean_url)
        if len(links) >= limit:
            break

    return links


def fetch_webpage(source: dict[str, Any], limit: int, fetched_at: str) -> list[dict[str, str]]:
    html = fetch_text(source["url"])
    links = article_links(source, html, limit)
    if not links:
        return [html_to_raw_item(source, str(source["url"]), html, fetched_at, is_list_page=True)]

    items: list[dict[str, str]] = []
    for link in links:
        try:
            article_html = fetch_text(link)
            items.append(html_to_raw_item(source, link, article_html, fetched_at, is_list_page=False))
        except Exception as error:
            write_log(f"failed article page: {link}: {error}")
    return items or [html_to_raw_item(source, str(source["url"]), html, fetched_at, is_list_page=True)]



def compact_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def tweet_urls(tweet: dict[str, Any]) -> list[str]:
    urls = tweet.get("entities", {}).get("urls", [])
    links: list[str] = []
    for item in urls:
        expanded_url = str(item.get("expanded_url") or item.get("url") or "").strip()
        if expanded_url:
            links.append(expanded_url)
    return links


def tweet_to_raw(
    source: dict[str, Any], tweet: dict[str, Any], users_by_id: dict[str, dict[str, Any]], fetched_at: str
) -> dict[str, str]:
    tweet_id = str(tweet.get("id") or "").strip()
    text = str(tweet.get("text") or "").strip()
    author = users_by_id.get(str(tweet.get("author_id") or ""), {})
    username = str(author.get("username") or "").strip()
    author_name = str(author.get("name") or "").strip()
    public_metrics = tweet.get("public_metrics") or {}
    title_text = compact_text(text)[:100]
    title = f"X: {title_text}" if title_text else f"X post {tweet_id}"
    url = f"https://x.com/{username}/status/{tweet_id}" if username else f"https://x.com/i/web/status/{tweet_id}"

    lines = []
    if author_name or username:
        handle = f"@{username}" if username else "unknown"
        lines.append(f"Author: {author_name or handle} ({handle})")
    if tweet_id:
        lines.append(f"Tweet ID: {tweet_id}")
    if public_metrics:
        lines.append(
            "Metrics: "
            f"{public_metrics.get('reply_count', 0)} replies, "
            f"{public_metrics.get('retweet_count', 0)} reposts, "
            f"{public_metrics.get('like_count', 0)} likes, "
            f"{public_metrics.get('quote_count', 0)} quotes"
        )
    if lines:
        lines.append("")
    lines.append(text or url)

    links = tweet_urls(tweet)
    if links:
        lines.extend(["", "Links:"])
        lines.extend(f"- {link}" for link in links)

    return {
        "title": title,
        "url": url,
        "source": str(source.get("name", "")),
        "source_type": str(source.get("type", "")),
        "published_at": str(tweet.get("created_at") or ""),
        "fetched_at": fetched_at,
        "content_type": "markdown",
        "is_list_page": "false",
        "content": "\n".join(lines),
    }


def fetch_x_recent_search(source: dict[str, Any], limit: int, fetched_at: str) -> list[dict[str, str]]:
    token_env = str(source.get("token_env") or "X_BEARER_TOKEN")
    token = secret_value(token_env)
    if not token:
        raise RuntimeError(f"missing env var {token_env}")

    query = str(source.get("query") or "").strip()
    if not query:
        raise RuntimeError("missing X API query")

    max_results = max(10, min(limit, 100))
    params = {
        "query": query,
        "max_results": str(max_results),
        "tweet.fields": "created_at,author_id,public_metrics,entities",
        "expansions": "author_id",
        "user.fields": "username,name",
    }
    url = str(source.get("url") or "https://api.x.com/2/tweets/search/recent")
    headers = {"Authorization": f"Bearer {token}", "User-Agent": "ai-radar/0.1"}

    with httpx.Client(timeout=20.0, follow_redirects=True) as client:
        response = client.get(url, headers=headers, params=params)

    if response.status_code in {401, 403}:
        raise RuntimeError(f"X API authentication failed: status {response.status_code}")
    if response.status_code == 402:
        raise RuntimeError("X API access requires a paid or eligible plan: status 402")
    if response.status_code == 429:
        raise RuntimeError("X API rate limited: status 429")
    if response.status_code >= 400:
        raise RuntimeError(f"X API request failed: status {response.status_code}")

    payload = response.json()
    tweets = payload.get("data") or []
    users = payload.get("includes", {}).get("users", [])
    users_by_id = {str(user.get("id")): user for user in users}
    items = [tweet_to_raw(source, tweet, users_by_id, fetched_at) for tweet in tweets[:limit]]
    if not items:
        raise RuntimeError("X API returned 0 posts")
    return items


def fetch_github_trending(source: dict[str, Any], limit: int, fetched_at: str) -> list[dict[str, str]]:
    html = fetch_text(source["url"])
    soup = BeautifulSoup(html, "html.parser")
    items: list[dict[str, str]] = []

    for repo in soup.select("article.Box-row")[:limit]:
        heading = repo.find("h2")
        link = heading.find("a", href=True) if heading else None
        if not heading or not link:
            continue
        title = " ".join(heading.get_text(" ", strip=True).split())
        url = urljoin("https://github.com", link["href"])
        description = repo.find("p")
        summary = description.get_text(" ", strip=True) if description else "No description."
        language = repo.find(attrs={"itemprop": "programmingLanguage"})
        stars_today = repo.find(string=re.compile("stars today"))
        meta = []
        if language:
            meta.append(f"Language: {language.get_text(' ', strip=True)}")
        if stars_today:
            meta.append(stars_today.strip())
        content = summary if not meta else summary + "\n\n" + "\n".join(f"- {item}" for item in meta)
        items.append(
            {
                "title": title,
                "url": url,
                "source": str(source.get("name", "")),
                "source_type": str(source.get("type", "")),
                "published_at": "",
                "fetched_at": fetched_at,
                "content_type": "markdown",
                "is_list_page": "false",
                "content": content,
            }
        )

    if not items:
        raise RuntimeError("GitHub Trending returned 0 repositories")
    return items


def raw_path_for(item: dict[str, str], run_date: str) -> Path:
    source_slug = slugify(item["source"])
    item_key = item.get("url") or item["title"]
    item_hash = hashlib.sha1(item_key.encode("utf-8")).hexdigest()[:10]
    item_slug = slugify(item["title"], 60)
    return RAW_DIR / run_date / source_slug / f"{item_slug}-{item_hash}.md"


def render_raw(item: dict[str, str]) -> str:
    return (
        "---\n"
        f"title: \"{yaml_scalar(item['title'])}\"\n"
        f"url: \"{yaml_scalar(item['url'])}\"\n"
        f"source: \"{yaml_scalar(item['source'])}\"\n"
        f"source_type: \"{yaml_scalar(item['source_type'])}\"\n"
        f"published_at: \"{yaml_scalar(item['published_at'])}\"\n"
        f"fetched_at: \"{yaml_scalar(item['fetched_at'])}\"\n"
        f"content_type: \"{yaml_scalar(item['content_type'])}\"\n"
        f"is_list_page: {yaml_scalar(item.get('is_list_page', 'false'))}\n"
        "---\n\n"
        f"{item['content'].strip()}\n"
    )


def save_raw_items(items: list[dict[str, str]], run_date: str) -> int:
    saved = 0
    for item in items:
        path = raw_path_for(item, run_date)
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_raw(item), encoding="utf-8")
        saved += 1
    return saved


def fetch_source(source: dict[str, Any], limit: int, fetched_at: str) -> list[dict[str, str]]:
    mode = source.get("mode")
    if mode == "rss":
        return fetch_rss(source, limit, fetched_at)
    if mode == "webpage":
        return fetch_webpage(source, limit, fetched_at)
    if mode == "github_trending":
        return fetch_github_trending(source, limit, fetched_at)
    if mode == "x_recent_search":
        return fetch_x_recent_search(source, limit, fetched_at)
    raise ValueError(f"unsupported mode: {mode}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch configured AI sources into raw markdown files.")
    parser.add_argument("--limit", type=int, default=10, help="Max entries per RSS source.")
    args = parser.parse_args()

    fetched_at = utc_now().isoformat()
    run_date = fetched_at[:10]
    sources = load_sources()

    total_saved = 0
    for source in sources:
        name = source.get("name", "unknown")
        try:
            items = fetch_source(source, args.limit, fetched_at)
            saved = save_raw_items(items, run_date)
            total_saved += saved
            message = f"fetched {name}: {len(items)} items, {saved} new raw files"
            print(message)
            write_log(message)
        except Exception as error:
            message = f"failed {name}: {error}"
            print(message)
            write_log(message)

    print(f"done: {total_saved} new raw files")


if __name__ == "__main__":
    main()
