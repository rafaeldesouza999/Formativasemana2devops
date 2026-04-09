from fastapi import FastAPI
from Jogo import mostrajogo


app = FastAPI()


@app.get("/Jogos")
def get_jogos():
    return mostrajogo()
