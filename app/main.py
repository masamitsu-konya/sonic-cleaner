from fastapi import FastAPI

from app.routers import jobs  # ルーター読み込み

app = FastAPI(title="Sonic Cleaner", version="0.1.0")

# /jobs ルートを登録
app.include_router(jobs.router)


@app.get("/ping")
async def ping():
    return {"message": "pong"}
