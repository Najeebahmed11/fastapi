from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel
import os

app = FastAPI()

# Retrieve the model and task names from the environment variables
model_name = os.getenv("MODEL_NAME", "bert-base-uncased") # Default if not set
task_name = os.getenv("TASK_NAME", "text-generation") # Default if not set

class RequestBody(BaseModel):
    text: str

@app.post("/run_model")
def run_model(request_body: RequestBody):
    try:
        # Initialize the pipeline with the model and task
        pipe = pipeline(task_name, model=model_name)
        result = pipe(request_body.text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"Hello": "from FastAPI", "model": model_name, "task": task_name}
