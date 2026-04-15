from fastapi.testclient import TestClient
from src.main import app
import sys
import os
sys.path.append(os.path.abspath("src"))


client = TestClient(app)

#Testa se retorna a lista
def test_lista_jogos():
    response = client.get("/Jogos")
    assert response.status_code == 200

#Testa a quantidade de jogos na lista
def test_quantidade_jogos():
    response = client.get("/Jogos")
    data = response.json()
    assert len(data) == 4

#Testa se contem o jogo específico
def test_contem_thewitcher3():
    response = client.get("/Jogos")
    data = response.json()
    nomes=[j["Nome"] for j in data]
    assert "The Witcher 3" in nomes

#Testa a estrutura do objeto Jogo
def test_estrutura_jogo():
    response = client.get("/Jogos")
    data = response.json()
    assert "ID" in data[0]
    assert "nome" in data[0]

#Testa o endpoint inválido
def test_rota_invalida():
    response = client.get("/naoexiste")
    assert response.status_code == 404