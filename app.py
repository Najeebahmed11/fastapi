from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()

class RequestBody(BaseModel):
    task: str
    model_name: str
    text: str

@app.post("/run_model")
def run_model(request_body: RequestBody):
    try:
        pipe = pipeline(request_body.task, model=request_body.model_name)
        result = pipe(request_body.text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mangum handler
handler = Mangum(app)
