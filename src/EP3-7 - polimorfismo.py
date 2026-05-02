'''
personagens (classe pai) -> mago e guerreiro (filhas)
batalha continua em turnos até a vida de algum <=0
main -> "roteiro"
'''

from abc import ABC, abstractmethod

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = float(vida)

    @abstractmethod
    def atacar(self, alvo):
        pass



class Guerreiro(Personagem):

    def __init__(self, nome, vida, forcaAtaque):
        super().__init__(nome, vida)
        self.forcaAtaque = float(forcaAtaque)

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}!")
        alvo.vida -= self.forcaAtaque  #atacando alvo
        print(f"{alvo.nome} tem {alvo.vida} de vida.")



class Mago(Personagem):

    def __init__(self, nome, vida, poderMagico):
        super().__init__(nome, vida)
        self.poderMagico = float(poderMagico) #add float no construtor, e n na main
        
    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}!")
        alvo.vida -= self.poderMagico*1.5 #atacando alvo
        print(f"{alvo.nome} tem {alvo.vida} de vida.")



def batalha(p1, p2): #não ataca, mas conduz a batalha e chama atacar()
    
    while p1.vida > 0 and p2.vida > 0:
        p1.atacar(p2)
        if p2.vida > 0:
            p2.atacar(p1)
    
    if p1.vida <= 0:
        print(f"{p1.nome} foi derrotado!")
        print(f"Batalha encerrada!")
    else:
        print(f"{p2.nome} foi derrotado!")
        print(f"Batalha encerrada!")

def criar_personagem(linha):

    atributos = linha.split()
    tipo = atributos[0]
    nome = atributos[1]
    vida = atributos[2]
    if tipo == "G":
        forcaAtaque = atributos[3]
        return Guerreiro(nome, vida, forcaAtaque)
    else:
        poderMagico = atributos[3]
        return Mago(nome, vida, poderMagico)    



def main(): #entrada, criação e execução
    linha1 = input()
    linha2 = input()
    
    personagem1 = criar_personagem(linha1)
    personagem2 = criar_personagem(linha2)
    
    batalha(personagem1, personagem2)

if __name__ == '__main__':
    main()