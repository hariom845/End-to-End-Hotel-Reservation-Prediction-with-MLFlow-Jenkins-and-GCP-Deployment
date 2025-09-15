End-to-End Hotel Reservation Prediction
(with MLFlow, Jenkins & GCP Deployment)

📌 Project Overview

This project demonstrates an end-to-end machine learning pipeline for predicting hotel reservations. It covers the entire lifecycle:

Data ingestion & preprocessing

Model training & evaluation

Experiment tracking with MLFlow

Automated CI/CD using Jenkins

Cloud deployment on Google Cloud Platform (GCP)

The goal is to build a scalable, reproducible ML system that can be deployed and monitored in production.

🚀 Features

✅ End-to-end ML pipeline (from raw data to predictions)

✅ Experiment tracking & model versioning with MLFlow

✅ Automated training, testing & deployment via Jenkins

✅ Containerized app using Docker

✅ Deployment on GCP (Cloud Run / GKE / Compute Engine)

✅ Modular & configurable codebase

🏗️ Architecture

        ┌──────────────┐
        │   Dataset    │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Preprocessing│
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Training   │  ← MLFlow (tracking metrics, params, models)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Packaging  │  ← Dockerized app
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Jenkins    │  ← CI/CD pipeline
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │     GCP      │  ← Cloud Deployment
        └──────────────┘

📂 Project Structure

├── application.py        # Flask/FastAPI app for serving predictions
├── Dockerfile            # Docker container setup
├── Jenkinsfile           # Jenkins pipeline definition
├── requirements.txt      # Python dependencies
├── setup.py              # Package setup
├── config/               # Configurations (YAML/JSON)
├── src/                  # Core ML code
│   ├── data_ingestion.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── prediction.py
├── pipeline/             # Workflow orchestration scripts
├── notebook/             # EDA & experimentation notebooks
├── utils/                # Helper functions
├── custom_jenkins/       # Jenkins custom setup
├── templates/            # Web UI templates
├── static/               # Static files (CSS, JS)
└── artifacts/            # Saved models, logs, outputs

2️⃣ Installation

# Clone the repo
git clone https://github.com/hariom845/End-to-End-Hotel-Reservation-Prediction-with-MLFlow-Jenkins-and-GCP-Deployment.git
cd End-to-End-Hotel-Reservation-Prediction-with-MLFlow-Jenkins-and-GCP-Deployment

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

3️⃣ Configuration

Update configs in config/ (paths, hyperparameters, GCP project details).
Set environment variables for MLFlow URI and GCP credentials.

🔄 CI/CD with Jenkins

The Jenkinsfile defines the automation pipeline:

1. Checkout code
2. Install dependencies
3. Run tests
4. Train & log model
5. Build Docker image
6. Push to GCP & deploy
You can configure Jenkins to trigger the pipeline on every git push.

☁️ Deployment on GCP
Using Docker

📊 Results & Evaluation
Models tracked with MLFlow (metrics: Accuracy, Precision, Recall, F1, etc.)
Best model selected & deployed

🔮 Future Improvements

- Hyperparameter tuning (Grid Search / Bayesian Opt)
- Additional ML models (e.g., LightGBM, Neural Nets)
- Enhanced monitoring (Prometheus, Grafana)
- Automated retraining with new data
- A/B testing for models in production

