# All Things LLMs
## Overview
This project implements a robust pipeline that integrates various NLP tools and frameworks.

    RAGStack/
    │
    ├── src/
    │   ├── data/
    │   │   ├── connectors/
    │   │   │   ├── __init__.py
    │   │   │   ├── base.py
    │   │   │   ├── snowflake.py
    │   │   │   ├── databricks.py
    │   │   │   └── file_system.py
    │   │   ├── preprocessors/
    │   │   │   ├── __init__.py
    │   │   │   ├── base.py
    │   │   │   ├── text.py
    │   │   │   └── tabular.py
    │   │   └── __init__.py
    │   │
    │   ├── vectorstores/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── qdrant.py
    │   │   └── faiss.py
    │   │
    │   ├── llm/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── openai.py
    │   │   └── huggingface.py
    │   │
    │   ├── retrieval/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   └── similarity.py
    │   │
    │   ├── rag/
    │   │   ├── __init__.py
    │   │   ├── pipeline.py
    │   │   └── prompt_templates.py
    │   │
    │   ├── evaluation/
    │   │   ├── __init__.py
    │   │   ├── metrics.py
    │   │   └── evaluator.py
    │   │
    │   └── utils/
    │       ├── __init__.py
    │       ├── config.py
    │       └── logging.py
    │
    ├── examples/
    │   ├── customer_support/
    │   │   ├── app.py
    │   │   └── config.yaml
    │   └── document_qa/
    │       ├── app.py
    │       └── config.yaml
    │
    ├── tests/
    │   ├── unit/
    │   │   ├── test_data_connectors.py
    │   │   ├── test_preprocessors.py
    │   │   ├── test_vectorstores.py
    │   │   └── test_rag_pipeline.py
    │   └── integration/
    │       ├── test_end_to_end.py
    │       └── test_performance.py
    │
    ├── docs/
    │   ├── getting_started.md
    │   ├── api_reference.md
    │   ├── examples.md
    │   └── contributing.md
    │
    ├── scripts/
    │   ├── setup_dev_environment.sh
    │   └── run_tests.sh
    │
    ├── .github/
    │   └── workflows/
    │       ├── ci.yml
    │       └── release.yml
    │
    ├── requirements.txt
    ├── setup.py
    ├── README.md
    ├── LICENSE
    └── .gitignore
