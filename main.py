from fastapi import FastAPI
from Jogo import mostrajogo


app = FastAPI()


@app.get("/")
async def root():
    return mostrajogo()
