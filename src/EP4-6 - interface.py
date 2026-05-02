#interface e polimorfismo

from typing import Protocol

class MetodoPagamento(Protocol):
    def pagar(self, valor): ...

class CartaoCredito:
    def pagar(self, valor):
        return f"Pagando R${valor:.1f} via Cartão de Crédito"

class Boleto:
    def pagar(self, valor):
        return f"Pagando R${valor:.1f} via Boleto"

class Pix:
    def pagar(self, valor):
        return f"Pagando R${valor:.1f} via Pix"


metodo = input()
valor = float(input())
dic = {"CartaoCredito": CartaoCredito(), "Boleto": Boleto(), "Pix": Pix()}[metodo]
print(dic.pagar(valor))