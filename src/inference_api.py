import joblib
import pandas as pd

def load_model():
    model = joblib.load("model.pkl")
    return model

def predict(data):
    model = load_model()
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return prediction