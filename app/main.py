from fastapi import FastAPI

app = FastAPI(title="Audio Clean API", version="0.1.0")

@app.get("/ping")
async def ping():
    return {"message": "pong"}
