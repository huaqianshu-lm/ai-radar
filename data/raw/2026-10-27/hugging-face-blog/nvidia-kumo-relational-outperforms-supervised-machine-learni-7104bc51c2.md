---
title: "NVIDIA Kumo Relational Outperforms Supervised Machine Learning on Relational Data, No Training Required"
url: "https://huggingface.co/blog/nvidia/kumo-relational"
source_url: "https://huggingface.co/blog/nvidia/kumo-relational"
canonical_url: "https://huggingface.co/blog/nvidia/kumo-relational"
source: "Hugging Face Blog"
source_type: "developer"
published_at: "2026-10-21T18:26:30+00:00"
fetched_at: "2026-10-27T01:51:13+00:00"
content_type: "markdown"
is_list_page: false
---

# NVIDIA Kumo Relational Outperforms Supervised Machine Learning on Relational Data, No Training Required

## TL;DR

NVIDIA Kumo Relational is a pre-trained relational foundation model that makes predictions directly on enterprise databases. Given a predictive query, it gathers historical examples as context examples and predicts outcomes such as churn, demand, or fraud in a single forward pass. It needs no task-specific training, no feature engineering, and no flattening of tables. Kumo Relational is the first few-shot foundation model to outperform supervised machine learning on common relational benchmarks. Across 41 tasks on 15 databases, it beats supervised relational deep learning models and expert-engineered gradient-boosted tree pipelines, and on the SAP SALT enterprise benchmark it surpasses AutoGluon ensembles by 8% in mean reciprocal rank (MRR). It scales to databases with 500B+ rows and works for humans and agents alike, through NVIDIA's open-source, GPU-native `structured-data-models` and `kumo-engine` libraries, or as an NVIDIA NIM.

- **Paper:** https://arxiv.org/abs/2604.12596
- **Model Code:** https://github.com/NVIDIA/structured-data-models
- **Model Weights:** https://huggingface.co/nvidia/Kumo-Relational
- **Client Code:** https://github.com/NVIDIA/structured-data-models-client
- **NIM Documentation:** https://docs.nvidia.com/sdgm/rfm/overview

## The Shift to Structured Data Foundation Models

Foundation models have already rewritten the playbook for language and vision. Not long ago, production NLP meant a dedicated model per task, each fed by its own pipeline of tokenization, lemmatization, and n-grams. LLMs made that stack largely obsolete for three reasons: they were more accurate than the best task-specific models, far simpler to put into production, and flexible enough to open a new era of agentic applications.

The same shift is now underway for structured data. Relational databases power the world's most critical business decisions, yet predictive modeling on them still requires weeks of feature engineering, task-specific training, and tuned pipelines. Structured data foundation models change that for the same three reasons:

**Better accuracy today:** As drop-in replacements, these models already beat many production pipelines, especially XGBoost. On RelBench V1 classification tasks, Kumo Relational outperforms gradient-boosted trees on expert-engineered features by nearly 4 AUROC points on average. On SAP SALT, it beats XGBoost on engineered features by 7 MRR points out of the box and by 13 MRR points after fine-tuning. These results make a compelling case for replacing production XGBoost pipelines with Kumo Relational.

**Simplicity and agility:** One pre-trained model replaces separate pipelines for individual tasks. A new prediction becomes a query instead of a project, so ML teams can finally take on use cases that traditional ML made too laborious to build at every level of the organization.

**Agents that can predict:** LLMs let agents read, write, and reason. Structured data foundation models let them anticipate what happens next, such as which customer will churn, and act on it. Kumo Relational is already built to be called by agents, and its Predictive Query Language (PQL) gives them a simple interface for asking predictive questions.

Today, we are introducing **Kumo Relational** (Paper, GitHub, HuggingFace), a pre-trained foundation model that brings this paradigm to relational data. Connect a database, describe what to predict, and get predictions in a single forward pass. No training required.

## How Kumo Relational Works

Most foundation models for structured data operate on a single flat table. Real-world data lives in relational databases instead: users connected to orders connected to products, all evolving over time. Flattening these relationships into one row through manual aggregation (*e.g.*, "average order value in the last 30 days") loses fine-grained structural signals and takes significant human effort.

Kumo Relational is a *Relational Foundation Model* that operates directly on the database, respecting its tables, foreign keys, and timestamps. It is pre-trained once on synthetic relational data that reflects real-world datasets and adapts to each new task through *in-context learning* by reasoning over context examples at inference time. Each example pairs a local subgraph around an entity at a point in time with its ground-truth target (*e.g.*, "this user churned" or "this item sold 142 units").

*Figure 1. Overview of the Kumo Relational system. Connect a database, specify a predictive query, and Kumo Relational handles the rest, from context generation to model inference.*

To make a prediction, Kumo Relational has to do three things: **(1)** understand the values within each table, **(2)** relate records across tables, and **(3)** relate context examples with known targets to the entity being predicted. Here is how it works:

*Figure 2. Kumo Relational architecture: (a) context input, (b) reasoning within tables, (c) reasoning across tables.*

**Automatic Context Generation:** Tasks are written in the Predictive Query Language (PQL), a declarative interface where you state what to predict rather than how. For temporal tasks, Kumo Relational replays historical database states: it samples entity-centric subgraphs up to an anchor timestamp and computes each target from events after that timestamp, while serving the model only the data from before it. This prevents data leakage.

**Reasoning Within Tables:** A lightweight network processes each table independently via column attention (relating values within a column) and row attention (relating features within a row). The model learns which columns and rows matter for the current prediction and filters out noise before it propagates.

**Reasoning Across Tables:** A larger network distributes the row embeddings across the relational structure via graph attention over primary-key/foreign-key relationships, followed by cross-sample attention across context examples. This is where relational reasoning happens, such as linking a user's profile to their transaction history. Because this stage works on row embeddings rather than on every cell in every table, the design avoids quadratic cost and scales to large contexts and deeper subgraphs.

## How Kumo Relational Was Built

Kumo Relational is pre-trained on entirely synthetic relational data simulated to reflect real-world relational databases with diverse predictive queries. Pre-training proceeds in stages, from single tables to increasingly complex relational structures.

The diverse relational databases needed for pre-training are rarely public, so synthetic data fills the gap. Kumo Relational's generator builds on the approach of PluRel (Kothapalli et al., ICML 2026), which extends single-table data generators to full relational databases. PluRel generates each database in three stages: a schema, foreign-key links between rows that cluster as they do in real data, and column values from Structural Causal Models with temporal trends and cross-table dependencies. Generation is lightweight, so pre-training data is effectively unlimited. Pre-training loss follows a power law as synthetic databases are added, with gains that carry over to real databases.

Through this pre-training, the model learns to filter, correlate, and aggregate information across tables instead of relying on fixed aggregations.

## Performance

In the paper, we evaluated Kumo Relational on 41 benchmarks across 15 relational databases from RelBench V1 and V2, SAP SALT, and 4DBInfer, spanning e-commerce, medical, enterprise, social, and academic domains. None of these datasets were seen in pre-training. Kumo Relational outperforms the strongest supervised models in both classification and regression, including relational deep learning models and expert-engineered tabular ensembles. It is the top-performing in-context learning model on the RelBench leaderboard. On RelArena-α, it sits on the accuracy-efficiency Pareto front:

*Figure 3. RelArena-α leaderboard as of 2026-09-21: Elo across tasks versus total task runtime (log scale). Kumo Relational is about 430× faster than rtl-plurel at similar accuracy.*

On the SAP SALT enterprise benchmark, Kumo Relational surpasses large AutoGluon ensembles by 8% in mean reciprocal rank (MRR), and fine-tuning extends its lead over AutoGluon to 16%. It also holds up under hard conditions: it performs well with as little as 0.2% of the training data as context, stays stable when up to 75% of foreign-key links are removed, and barely degrades when noisy columns are added.

## Limitations

Kumo Relational performs best on data with meaningful relationships and temporal dynamics, such as user behavior over time. On tasks with very large training sets, task-specific supervised models may still edge out in-context predictions. Predictive signals must be reachable within a limited number of hops.

## Demo

Kumo Relational runs in-context learning natively over databases: in memory, through database and warehouse connectors, or through `kumo-engine` that handles 500B+ rows via memory-mapped I/O at up to 5 GB/s. The model itself is available in NVIDIA's newly released, GPU-native `structured-data-models` library, the same open-source library that powers our sister model, Kumo Tabular. The library downloads the weights from the Hugging Face Hub on first use, so you can load the model in a GPU-backed notebook and predict directly from it. The interface is designed to naturally extend tabular foundation models to relational signal by passing additional related multi-table context and query information:

```
import sdm  # pip install structured-data-models
model = sdm.models.KumoRelational(device="cuda")
pred = model(
    # In-context training table (fkeys/timestamps/targets):
    x_context=sdm.TableTensor(...),
    y_context=sdm.TableTensor(...),
    # Prediction examples (fkeys/timestamps):
    x_query=sdm.TableTensor(...),
    # Multi-table information for context/prediction entities:
    related_context_tables=sdm.RelatedTables(tables={...}),
    related_query_tables=sdm.RelatedTables(tables={...}),
)
```
See the library's relational examples for RelBench and SAP SALT pipelines.

To run the model as a separate service instead, deploy it as an NVIDIA NIM and point the open-source `structured-data-models-client` at it from your notebook. You write the prediction in PQL, and the client gathers the context examples and related tables, then sends the request:

```
import sdm_client  # pip install 'structured-data-models-client[relational]'
client = sdm_client.SDMClient(url="http://localhost:8001")  # NIM URL
query = sdm_client.PredictiveQuery(
    # Prediction task in Predictive Query Language (PQL):
    "PREDICT COUNT(orders.*, 0, 30, days) FOR EACH users.user_id",
    # Multi-table data as pandas DataFrames (keys/links inferred):
    {"users": ..., "orders": ...},
)
pred = client.predict(
    # Context examples and related tables for the entities to predict:
    query.materialize(indices=[1, 2, 3]),
    model=sdm_client.KumoRelational(),
)
```
See the client's example notebooks for end-to-end runs against a local NIM and on Databricks.

## Start Building with NVIDIA Kumo Relational

NVIDIA Kumo Relational is available today. Read the research paper, explore the quickstart notebook, or start making predictions on your own data. The code is released under the Apache 2.0 license and the model weights under the OpenMDW License Agreement, version 1.1. NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report model quality, risk, security vulnerabilities, or NVIDIA AI concerns here.

- **Paper:** https://arxiv.org/abs/2604.12596
- **Model Code:** https://github.com/NVIDIA/structured-data-models
- **Model Weights:** https://huggingface.co/nvidia/Kumo-Relational
- **Client Code:** https://github.com/NVIDIA/structured-data-models-client
- **NIM Documentation:** https://docs.nvidia.com/sdgm/rfm/overview
- **Quickstart notebook:** https://github.com/NVIDIA/structured-data-models-client/blob/main/examples/local/relational.ipynb
- **Related Research:** Predictive Query Language (PQL), PluRel, Kumo Tabular, TabICLv2

## Acknowledgements

We thank the entire Kumo team for their invaluable support. Special thanks go to Adi Wadaskar, Hema Raghavan, Manush Murali, Zack Drach, Vanja Josifovski, Myungwhan Kim, Siyang Xie, Alan Krumholz, Effy Fang, Abdullah Al-chihabi, Disha Dubey, Devan Johnson, Joseph Oliveira, Angela Liu, Miha Pelko, Vedaant Jain, Sally Liu, Aleksandar S. Sokolovski, and Alex Porter.
