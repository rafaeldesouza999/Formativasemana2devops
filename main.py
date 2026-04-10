from fastapi import FastAPI
from Jogo import mostrajogo

#Teste01
app = FastAPI()


@app.get("/Jogos")
def get_jogos():
    return mostrajogo()
