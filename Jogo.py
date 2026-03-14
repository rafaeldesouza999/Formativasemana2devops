
# Cria  a classe jogo
class Jogo:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero
    def __repr__(self):
        return f"{self.nome} {self.genero}"

# Cria lista de carros
Lista_Jogos = []

# cria os jogos
jogo1 = Jogo("the witcher 3 ", " RPG")
jogo2 = Jogo("NFS Most Wanted", "Corrida")
#Adiciona mais jogos
jogo3 = Jogo(" Elden Ring", " Souls Like")
jogo4 = Jogo("Genshin Impact", " RPG ")

# adiciona jogos na lista
Lista_Jogos.append(jogo1)
Lista_Jogos.append(jogo2)

print(" Ola´esse sao nossos jogos: ")
print(Lista_Jogos)