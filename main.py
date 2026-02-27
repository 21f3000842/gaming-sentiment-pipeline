from fastapi import FastAPI
import pandas as pd
import os

app=FastAPI()

#Path to analyzed data
DATA_PATH = "data/analyzed_headlines.csv"

@app.get("/")
def home():
    return {"message": "Welcome to the Gaming API", "status":"Online"}

@app.get("/sentiment")
def get_sentiment():
    #Check if file exists
    if not os.path.exists(DATA_PATH):
        return {"error": "File not found. Please run the ML pipeline first"}
    
    #Load the analyzed data
    df = pd.read_csv(DATA_PATH)

    #Convert Df to dict(JSON)
    results = df.to_dict(orient="records")

    return {
        'count': len(results),
        'data': results
    }

@app.get("/summary")
def get_summary():
    #Check if file exists
    if not os.path.exists(DATA_PATH):
        return {"error": "File not found. Please run the ML pipeline first"}
    
    df = pd.read_csv(DATA_PATH)
    summary=df['sentiment'].value_counts().to_dict()
    return {"summary": summary}