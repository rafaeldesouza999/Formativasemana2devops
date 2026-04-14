from src.main import *
from src.Jogo import *
from unittest.mock import patch

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

#Testa se retorna a lista
def test_Lista_Jogos():
    response = client.get("/jogos")
    assert response.status_code == 200

#Testa a quantidade de jogos na lista
def test_quantidade_jogos():
    response = client.get("/jogos")
    data = response.json()
    assert len(data) == 3

#Testa se contem o jogo específico
def test_contem_theWitcher3():
    response = client.get("/jogos")
    data = response.json()
    nomes=[j["nome"] for j in data]
    assert "the wicther 3 " in nomes

#Testa a estrutura do objeto Jogo
def test_estrutura_jogo():
    response = client.get("/jogos")
    data = response.json()
    assert "id" in data[0]
    assert "nome" in data[0]

#Testa o endpoint inválido
def test_rota_invalida():
    response = client.get("/naoexiste")
    assert response.status_code == 404