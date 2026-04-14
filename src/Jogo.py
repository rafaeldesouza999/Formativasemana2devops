

class Jogo:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero
    def __repr__(self):
        return f"{self.nome} {self.genero}"


def get_jogos():
    return mostrajogo()

# Cria  a classe jogo.

# Cria lista de carros
Lista_Jogos = []

# cria os jogos
jogo1 = Jogo("The Witcher 3 ", " RPG")
jogo2 = Jogo("NFS Most Wanted", "Corrida")
#Adiciona mais jogos
jogo3 = Jogo("Elden Ring", " Souls Like")
jogo4 = Jogo("Genshin Impact", " RPG ")

# adiciona jogos na lista
Lista_Jogos.append(jogo1)
Lista_Jogos.append(jogo2)
# adiciona os outros dois jogos a lista
Lista_Jogos.append(jogo3)
Lista_Jogos.append(jogo4)
print("Olá esses são nossos jogos: ")
#exibindo melhor



def mostrajogo():
    return [{"Nome ": Jogo.nome,"Gênero " : Jogo.genero}for Jogo in Lista_Jogos]


print(mostrajogo())

