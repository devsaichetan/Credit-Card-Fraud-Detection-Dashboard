# 💳 Credit Card Fraud Detection Dashboard

## 🚀 Overview

An AI-powered Credit Card Fraud Detection Dashboard built using **FastAPI**, **Machine Learning**, and **Interactive Analytics**.

This system detects fraudulent credit card transactions in real time and supports bulk CSV analysis with detailed fraud insights, risk assessment, and visual analytics.

---

## ✨ Features

### 🔍 Single Transaction Prediction

* Predict whether a transaction is Fraudulent or Legitimate
* Real-time probability scoring
* Risk level classification (Low / Medium / High)

### 📂 CSV Batch Analysis

* Upload CSV files containing thousands of transactions
* Bulk fraud detection
* Instant fraud summary

### 📊 Interactive Dashboard

* Total Transactions Analyzed
* Fraud Transactions Detected
* Fraud Percentage
* Risk Assessment
* Analysis History

### 📈 Visual Analytics

* Pie Chart Visualization
* Fraud vs Normal Distribution
* Fraud Alert Monitoring
* Transaction Insights

### ⚡ FastAPI Backend

* RESTful API Architecture
* Swagger Documentation
* High Performance Inference
* Production Ready Deployment

---

## 🧠 Machine Learning Pipeline

### Data Preprocessing

* Missing Value Handling
* Feature Scaling
* Standardization

### Imbalanced Data Handling

* SMOTE Oversampling

### Model Training

* Random Forest Classifier

### Evaluation Metrics

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

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* GitHub
* Render

---

## 📸 Dashboard Preview

### Home Dashboard

Add screenshot here

### CSV Analysis

Add screenshot here

### Fraud Analytics

Add screenshot here

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/devsaichetan/Credit-Card-Fraud-Detection-Dashboard.git
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

| Method | Endpoint     | Description           |
| ------ | ------------ | --------------------- |
| GET    | /            | Home                  |
| GET    | /health      | Health Check          |
| GET    | /model-info  | Model Information     |
| POST   | /predict     | Single Prediction     |
| POST   | /predict-csv | CSV Batch Prediction  |
| GET    | /docs        | Swagger Documentation |
| GET    | /ui          | Dashboard Interface   |

---

## 🎯 Future Enhancements

* Real-time Transaction Monitoring
* Live Fraud Alerts
* User Authentication
* Advanced Analytics Dashboard
* Email Notifications
* Cloud Database Integration
* Explainable AI (XAI)
* Deep Learning Models

---

## 👨‍💻 Developer

**Sai Chetan**

B.Tech CSE | Machine Learning Enthusiast | FastAPI Developer

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork this repository

🚀 Contribute to the project

---

### "Turning Transaction Data into Fraud Intelligence."
