"""
Simple FastAPI application demonstrating dependency usage
"""
from fastapi import FastAPI
import requests
import pandas as pd

app = FastAPI(title="Dependabot Demo API")


@app.get("/")
def read_root():
    return {
        "message": "Dependabot Security Demo",
        "status": "active",
        "dependencies": ["fastapi", "requests", "pandas"]
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/fetch-data")
def fetch_external_data():
    """Example using requests library"""
    try:
        response = requests.get("https://api.github.com/zen", timeout=5)
        return {"github_zen": response.text}
    except Exception as e:
        return {"error": str(e)}


@app.get("/data-info")
def data_info():
    """Example using pandas"""
    df = pd.DataFrame({
        "library": ["fastapi", "requests", "pandas"],
        "purpose": ["Web Framework", "HTTP Client", "Data Analysis"]
    })
    return {"data": df.to_dict(orient="records")}
