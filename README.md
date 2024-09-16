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
