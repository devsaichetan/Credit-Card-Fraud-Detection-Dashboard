from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
import joblib
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
import io
from fastapi.responses import FileResponse

# ==========================================
# LOAD MODEL & SCALERS
# ==========================================

model = joblib.load("models/credit_fraud_model.pkl")
amount_scaler = joblib.load("models/amount_scaler.pkl")
time_scaler = joblib.load("models/time_scaler.pkl")

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="""
Machine Learning API for detecting fraudulent credit card transactions.

Features:
- Random Forest Classifier
- SMOTE Oversampling
- Hyperparameter Tuning
- Fraud Risk Analysis
- Probability Scoring
""",
    version="1.0.0"
)

# ==========================================
# TEMPLATES & STATIC FILES
# ==========================================

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# ==========================================
# INPUT SCHEMA
# ==========================================

class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# ==========================================
# HOME
# ==========================================

@app.get("/", tags=["General"])
def home():
    return {
        "project": "Credit Card Fraud Detection API",
        "version": "1.0.0",
        "model": "Random Forest Classifier",
        "status": "Active",
        "developer": "Sai Chetan"
    }

# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health", tags=["Monitoring"])
def health():
    return {
        "status": "healthy",
        "model_loaded": True,
        "api_running": True
    }

# ==========================================
# MODEL INFO
# ==========================================

@app.get("/model-info", tags=["Model"])
def model_info():
    return {
        "model_name": "Random Forest Classifier",
        "problem_type": "Binary Classification",
        "dataset": "Credit Card Fraud Detection",
        "features": 30,
        "classes": {
            "0": "Normal Transaction",
            "1": "Fraud Transaction"
        },
        "preprocessing": [
            "StandardScaler(Time)",
            "StandardScaler(Amount)",
            "SMOTE"
        ]
    }

# ==========================================
# METRICS
# ==========================================

@app.get("/metrics", tags=["Monitoring"])
def metrics():
    return {
        "model": "Random Forest",
        "version": "1.0.0",
        "features": 30,
        "status": "Running"
    }

# ==========================================
# FRONTEND
# ==========================================

@app.get("/ui")
async def frontend(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# ==========================================
# PREDICTION
# ==========================================

@app.post("/predict", tags=["Prediction"])
def predict(transaction: Transaction):

    df = pd.DataFrame([transaction.model_dump()])

    # Apply same preprocessing used during training

    df["Amount"] = amount_scaler.transform(
        df[["Amount"]]
    )

    df["Time"] = time_scaler.transform(
        df[["Time"]]
    )

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    if probability > 0.80:
        risk_level = "High"
    elif probability > 0.40:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "prediction": int(prediction),
        "prediction_label":
            "Fraud Transaction"
            if prediction == 1
            else "Normal Transaction",

        "fraud_probability_percent":
            round(float(probability) * 100, 2),

        "risk_level": risk_level,

        "model_version": "1.0.0",

        "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
    }
@app.post("/predict-csv", tags=["Prediction"])
async def predict_csv(file: UploadFile = File(...)):

    try:

        # Read uploaded CSV
        contents = await file.read()

        df = pd.read_csv(
            io.StringIO(
                contents.decode("utf-8")
            )
        )

        # Remove target column if present
        if "Class" in df.columns:
            df = df.drop("Class", axis=1)

        # Apply same preprocessing
        df["Amount"] = amount_scaler.transform(
            df[["Amount"]]
        )

        df["Time"] = time_scaler.transform(
            df[["Time"]]
        )

        # Predict
        predictions = model.predict(df)

        probabilities = model.predict_proba(df)[:, 1]

        # Add prediction columns
        df["Prediction"] = predictions


        df["Fraud_Probability"] = (
            probabilities * 100
        ).round(2)

        top_alerts = []

        top_df = (
            df.sort_values(
                "Fraud_Probability",
                ascending=False
            )
            .head(5)
        )

        for idx, row in top_df.iterrows():

            top_alerts.append({

                "transaction_id":
                    int(idx),

                "probability":
                    float(
                        row["Fraud_Probability"]
                    ),

                "risk":
                    "Critical"

            })
        
        fraud_count = int(
            (predictions == 1).sum()
        )

        normal_count = int(
            (predictions == 0).sum()
        )

        total = len(df)

        return {
        "total_transactions": total,
        "fraud_transactions": fraud_count,
        "normal_transactions": normal_count,
        "fraud_percentage": round(
            (fraud_count / total) * 100,
            2
        ),
        "top_alerts": top_alerts,
        "sample_results": df.head(10).to_dict(
            orient="records"
        )
    }

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )