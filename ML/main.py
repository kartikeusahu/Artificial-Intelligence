# FastAPI framework import
from fastapi import FastAPI

# CORS middleware import (Frontend ko API access dene ke liye)
from fastapi.middleware.cors import CORSMiddleware

# Request body validation ke liye BaseModel
from pydantic import BaseModel

# Machine Learning ka Linear Regression model
from sklearn.linear_model import LinearRegression

# Numerical calculations ke liye NumPy
import numpy as np

# CSV file read karne ke liye Pandas
import pandas as pd


# FastAPI application create karna
app = FastAPI()


# CORS enable karna taaki koi bhi frontend API ko access kar sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Sabhi origins allow
    allow_credentials=True,   # Credentials allow
    allow_methods=["*"],      # Sabhi HTTP methods allow
    allow_headers=["*"],      # Sabhi headers allow
)


# CSV dataset load karna
df = pd.read_csv("dataset/house_data.csv")


# Input features select karna
X = df[["Area_sqft", "Bedrooms", "Age_years"]]

# Target column (House Price)
Y = df["Price"]


# Linear Regression model create karna
model = LinearRegression()

# Model ko training data se train karna
model.fit(X, Y)


# API me input data ka format define karna
class HouseInput(BaseModel):

    # House ka area (square feet)
    Area_sqft: float

    # Bedrooms ki sankhya
    Bedrooms: int

    # House ki age (years me)
    Age_years: int


# POST API endpoint create karna
@app.post("/predict")
def predict_price(input: HouseInput):

    # User ke input ko NumPy array me convert karna
    features = np.array([
        [input.Area_sqft, input.Bedrooms, input.Age_years]
    ])

    # Trained model se prediction lena
    price = model.predict(features)

    # Prediction ko JSON format me return karna
    return {
        "predicted_price": int(price[0])
    }