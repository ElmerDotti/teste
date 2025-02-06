from fastapi import FastAPI
from analysis_service import process_sessions

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await process_sessions()

@app.get("/")
async def root():
    return {"message": "Serviço de Análise de Conversas rodando!"}
