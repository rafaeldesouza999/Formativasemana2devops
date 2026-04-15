

class Jogo:
    def __init__(self,ID, nome, genero):
        self.idjogo = ID
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
jogo1 = Jogo(1,"The Witcher 3 ", " RPG")
jogo2 = Jogo(2,"NFS Most Wanted", "Corrida")
#Adiciona mais jogos
jogo3 = Jogo(3,"Elden Ring", " Souls Like")
jogo4 = Jogo(4,"Genshin Impact", " RPG ")

# adiciona jogos na lista
Lista_Jogos.append(jogo1)
Lista_Jogos.append(jogo2)
# adiciona os outros dois jogos a lista
Lista_Jogos.append(jogo3)
Lista_Jogos.append(jogo4)
print("Olá esses são nossos jogos: ")
#exibindo melhor



def mostrajogo():
    return [{"ID": Jogo.idjogo, "Nome ": Jogo.nome,"Gênero " : Jogo.genero}for Jogo in Lista_Jogos]


print(mostrajogo())

