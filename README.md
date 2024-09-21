# Machine Learning Experimentation Pipeline

## Overview
This project implements a robust machine learning experimentation pipeline that integrates various tools and frameworks. It emphasizes principles of reproducibility, tracking, and collaboration, enabling data scientists and machine learning engineers to efficiently manage their experiments.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Overview](#pipeline-overview)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Installation
To install the necessary dependencies, run:

## Usage
To start the experimentation process, run the following command:

## Pipeline Overview
The pipeline consists of the following key components:

1. **Data Acquisition**: Fetch datasets using `fetch_openml` or other data sources.
2. **Data Preprocessing**: Split the data into training and testing sets using `train_test_split`.
3. **Model Training**: Train models using various algorithms (e.g., `RandomForestRegressor`, `LogisticRegression`).
4. **Experiment Tracking**: Log parameters, metrics, and models using MLflow and Weights & Biases (W&B) for reproducibility and analysis.
5. **Model Evaluation**: Evaluate model performance using metrics like Mean Squared Error (MSE) and classification reports.
6. **Deployment**: Deploy models to cloud platforms or local environments as needed.

## Configuration
Configuration files are located in the `gcp` directory. Key files include:
- `gcp/deployment.yml`
- `gcp/Dockerfile`

## Development
### Setting Up
1. Clone the repository:
    ```shell
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```shell
    cd <project-directory>
    ```
3. Install dependencies:
    ```shell
    pip install -r requirements.txt
    ```

### Running Locally
To run the application locally, ensure that the MLflow tracking server is running on `http://127.0.0.1:5001`.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


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