from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import export_frontend_data as exporter


def sample_item() -> dict[str, str]:
    return {
        "id": "item-1",
        "title": "Example AI model",
        "summary": "An example model was released.",
        "source": "Example",
        "source_type": "official",
        "display_time": "2026-08-12T00:00:00Z",
        "time_type": "published",
        "url": "https://example.com/news/?utm_source=test#section",
    }


class TranslationCacheTest(unittest.TestCase):
    def test_new_translation_is_cached_and_reused(self) -> None:
        item = sample_item()
        translation = {"title": "示例 AI 模型", "summary": "一个示例模型已发布。"}

        with tempfile.TemporaryDirectory() as directory:
            with patch.object(exporter, "TRANSLATIONS_DIR", Path(directory)):
                with patch.object(
                    exporter,
                    "gemini_api_key",
                    return_value="test-key",
                ), patch.object(
                    exporter,
                    "translate_items",
                    return_value={item["id"]: translation},
                ) as translate:
                    translated, translated_count = exporter.translated_frontend_items(
                        [item]
                    )

                self.assertEqual(translated_count, 1)
                self.assertEqual(translated[0]["title"], translation["title"])
                self.assertEqual(translated[0]["summary"], translation["summary"])
                translate.assert_called_once()

                with patch.object(
                    exporter,
                    "translate_items",
                    side_effect=AssertionError("cache was not used"),
                ):
                    cached, cached_count = exporter.translated_frontend_items([item])

                self.assertEqual(cached_count, 0)
                self.assertEqual(cached, translated)

    def test_missing_key_does_not_create_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            cache_dir = Path(directory)
            with patch.object(exporter, "TRANSLATIONS_DIR", cache_dir), patch.object(
                exporter, "gemini_api_key", return_value=""
            ):
                with self.assertRaisesRegex(RuntimeError, "GEMINI_API_KEY"):
                    exporter.translated_frontend_items([sample_item()])

            self.assertEqual(list(cache_dir.iterdir()), [])

    def test_translation_requires_chinese_title_and_summary(self) -> None:
        with self.assertRaisesRegex(ValueError, "summary is not Chinese"):
            exporter.validate_translation(
                {"id": "item-1", "title": "English", "summary": "English summary"},
                "item-1",
            )

    def test_proper_name_title_uses_translated_summary_as_chinese_fallback(self) -> None:
        translation = exporter.validate_translation(
            {
                "id": "item-1",
                "title": "3b1b / manim",
                "summary": "用于制作数学讲解视频的动画引擎。使用 Python 开发。",
            },
            "item-1",
        )

        self.assertEqual(
            translation["title"],
            "3b1b / manim：用于制作数学讲解视频的动画引擎",
        )

    def test_gemini_request_uses_current_flash_lite_structured_output(self) -> None:
        item = sample_item()
        response_body = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": (
                                    '[{"id":"item-1","title":"示例 AI 模型",'
                                    '"summary":"一个示例模型已发布。"}]'
                                )
                            }
                        ]
                    }
                }
            ]
        }
        response = SimpleNamespace(
            raise_for_status=lambda: None,
            json=lambda: response_body,
        )

        with patch.object(exporter.httpx, "post", return_value=response) as post:
            translated = exporter.translate_items([item], "test-key")

        request = post.call_args.kwargs
        self.assertIn("gemini-3.5-flash-lite", post.call_args.args[0])
        self.assertEqual(request["headers"]["x-goog-api-key"], "test-key")
        self.assertEqual(
            request["json"]["generationConfig"]["responseMimeType"],
            "application/json",
        )
        self.assertEqual(
            request["json"]["generationConfig"]["responseSchema"]["type"],
            "ARRAY",
        )
        prompt = request["json"]["contents"][0]["parts"][0]["text"]
        self.assertIn("原始 title 只有产品名、仓库名", prompt)
        self.assertEqual(translated[item["id"]]["title"], "示例 AI 模型")


if __name__ == "__main__":
    unittest.main()
