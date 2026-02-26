from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app = FastAPI()

class TestIn(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Deu certo o GET"}

@app.get("/health")
async def healt():
    return {"message": "saúde ?"}

@app.post('/test')
async def tesst(data: TestIn):
    return {"message": data.message}

if __name__ == "__main__":
    uvicorn.run("main:app")