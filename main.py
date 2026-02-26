from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Deu certo o GET"}

@app.get("/health")
async def healt():
    return {"message": "saúde ?"}

if __name__ == "__main__":
    uvicorn.run("main:app")