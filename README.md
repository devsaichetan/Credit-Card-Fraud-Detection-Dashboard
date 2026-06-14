# 💳 Credit Card Fraud Detection Dashboard

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Live-green)
![Machine%20Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Deployment](https://img.shields.io/badge/Deployment-Render-purple)

## 🚀 Overview

An AI-powered Credit Card Fraud Detection Dashboard built using **FastAPI**, **Machine Learning**, and **Interactive Analytics**.

The system detects fraudulent credit card transactions in real-time and supports bulk CSV analysis with detailed fraud insights, risk assessment, and visualization dashboards.

This project demonstrates the complete Machine Learning lifecycle including data preprocessing, handling imbalanced datasets, model training, deployment, and real-world API integration.

---

## 🌐 Live Demo

### Dashboard

https://credit-card-fraud-detection-dashboard-orpr.onrender.com/ui

### API Documentation

https://credit-card-fraud-detection-dashboard-orpr.onrender.com/docs

---

## ✨ Features

### 🔍 Single Transaction Prediction

* Predict whether a transaction is Fraudulent or Legitimate
* Real-time fraud probability scoring
* Risk level classification

### 📂 CSV Batch Analysis

* Upload CSV files for bulk fraud detection
* Analyze thousands of transactions instantly
* Generate fraud statistics

### 📊 Interactive Dashboard

* Total Transactions
* Fraud Transactions
* Normal Transactions
* Fraud Percentage
* Risk Assessment
* Analysis History

### 📈 Analytics & Visualization

* Pie Chart Visualization
* Fraud Distribution Analysis
* Fraud Alert Monitoring
* Transaction Insights

### ⚡ FastAPI Backend

* RESTful API Architecture
* Swagger Documentation
* High Performance Inference
* Cloud Deployment Ready

---

## 🧠 Machine Learning Pipeline

### Data Preprocessing

* Data Cleaning
* Feature Scaling
* Standardization
* Feature Selection

### Handling Imbalanced Data

* SMOTE (Synthetic Minority Oversampling Technique)

### Model Training

* Random Forest Classifier

### Model Evaluation

* Accuracy
* Precision
* Recall
* F1 Score

---

## 🏗️ Project Structure

```text
Credit-Card-Fraud-Detection-Dashboard/
│
├── app.py
├── Procfile
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── credit_fraud_model.pkl
│   ├── amount_scaler.pkl
│   └── time_scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshots/
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Imbalanced-Learn (SMOTE)
* Joblib

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* GitHub
* Render

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/devsaichetan/Credit-Card-Fraud-Detection-Dashboard.git
```

### Navigate to Project

```bash
cd Credit-Card-Fraud-Detection-Dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app:app --reload
```

### Open Browser

```text
http://127.0.0.1:8000/ui
```

---

## 📡 API Endpoints

| Method | Endpoint     | Description                   |
| ------ | ------------ | ----------------------------- |
| GET    | /            | Home Endpoint                 |
| GET    | /health      | Health Check                  |
| GET    | /model-info  | Model Information             |
| POST   | /predict     | Single Transaction Prediction |
| POST   | /predict-csv | CSV Batch Prediction          |
| GET    | /metrics     | Model Metrics                 |
| GET    | /docs        | Swagger Documentation         |
| GET    | /ui          | Dashboard Interface           |

---

## 🚀 Deployment

This application is publicly deployed using Render.

### Deployment Stack

* Render Cloud Platform
* FastAPI Backend
* Random Forest Machine Learning Model
* Interactive Frontend Dashboard

---

## 🎯 Future Enhancements

* User Authentication System
* Advanced Fraud Risk Dashboard
* Real-Time Transaction Monitoring
* Explainable AI (XAI)
* Deep Learning Based Detection
* Email & SMS Fraud Alerts
* Cloud Database Integration
* Multi-Model Fraud Detection Pipeline
* Advanced Analytics Dashboard

---

## 👨‍💻 Developer

### Sai Chetan

B.Tech Computer Science Engineering

Machine Learning • Artificial Intelligence • FastAPI • Data Science

Passionate about building AI-powered solutions that solve real-world problems through machine learning and intelligent analytics.

---

## ⚠️ Usage Notes

### CSV Upload Guidelines

To ensure smooth performance on the public demo deployment:

* Upload CSV files containing **50,000 rows or fewer**
* Very large datasets may exceed the memory limits of the free cloud hosting environment
* For best performance, use datasets between **1,000 and 10,000 rows**
* The application is optimized for demonstration and educational purposes

### Expected CSV Format

The uploaded file must contain:

* Time
* V1 to V28
* Amount

The target column (`Class`) is optional for prediction but can be included for comparison and validation.

### Demo Deployment Limitations

This application is currently deployed on a free cloud instance with limited memory resources.

For enterprise-scale datasets, a higher-capacity deployment environment is recommended.
 
----

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork this repository

🚀 Contribute to the project

---

## 📜 License

This project is licensed under the MIT License.

---

### 💡 Turning Transaction Data into Fraud Intelligence.
