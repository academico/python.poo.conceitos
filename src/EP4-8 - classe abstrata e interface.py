from typing import Protocol
from abc import ABC, abstractmethod


#classe abstrata
class Veiculo(ABC):
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    @abstractmethod #obriga todas as filhas a terem esse método
    def calcularImposto(self):
        pass


#interface
class Eletrico(Protocol):
    def autonomiaBateria(self): ...



#classes filhas da superclasse abstrata ('SAO UM' veiculo)
class Carro(Veiculo):
    def __init__(self, marca, preco):
        super().__init__(marca, preco)

    def calcularImposto(self):
        return 0.15*self.preco


class Moto(Veiculo):
    def __init__(self, marca, preco):
        super().__init__(marca, preco)

    def calcularImposto(self):
        return 0.08*self.preco



#classes que implementam os métodos da interface, sendo compatível com ela ('PODEM FAZER')
class CarroEletrico(Carro):
    def __init__(self, marca, preco, autonomia):
        super().__init__(marca, preco)
        self.autonomia = autonomia

    def calcularImposto(self):
        return 0.15*self.preco

    def autonomiaBateria(self):
        return self.autonomia


class MotoEletrica(Moto):
    def __init__(self, marca, preco, autonomia):
        super().__init__(marca, preco)
        self.autonomia = autonomia

    def calcularImposto(self):
        return 0.08*self.preco

    def autonomiaBateria(self):
        return self.autonomia


def cria_objeto(tipo, marca, preco, autonomia=None):
    if autonomia is not None: #tem autonomia
        if tipo == 'CARRO':
            veiculo = CarroEletrico(marca, preco, autonomia)
        else:
            veiculo = MotoEletrica(marca, preco, autonomia)
    else:
        if tipo == 'CARRO':
            veiculo = Carro(marca, preco)
        else:
            veiculo = Moto(marca, preco)
    print(f"Preço: {veiculo.preco:.2f}")
    print(f"Imposto: {veiculo.calcularImposto():.2f}")
    print(f"Total: {veiculo.preco + veiculo.calcularImposto():.2f}")
    if autonomia is not None:
        print(f"Autonomia: {veiculo.autonomiaBateria()} km")


def main():
    tipo = input()
    marca = input()
    preco = float(input())
    try:
        autonomia_input = input()
        if len(autonomia_input) != 0:
          cria_objeto(tipo, marca, preco, int(autonomia_input))
    except EOFError:
        autonomia = None
        cria_objeto(tipo, marca, preco, autonomia)


if __name__ == "__main__":
    main()