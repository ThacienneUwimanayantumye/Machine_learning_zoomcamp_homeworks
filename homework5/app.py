import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Load the pipeline
with open('pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)

app = FastAPI()

class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post("/predict")
def predict(lead: Lead):
    # Convert to dictionary
    lead_dict = lead.model_dump()
    
    # Get prediction probability
    probability = pipeline.predict_proba([lead_dict])[0, 1]
    
    return {
        "probability": float(probability)
    }

@app.get("/")
def root():
    return {"message": "Lead Scoring API"}

