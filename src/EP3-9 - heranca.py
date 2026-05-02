class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def contar_descendentes(self):
        total_descendentes = len(self.filhos)
        for filho in self.filhos:
            total_descendentes += filho.contar_descendentes()
        return total_descendentes


def obter_pessoa(nome, pessoas):
    if nome not in pessoas:
        pessoas[nome] = Pessoa(nome)
    return pessoas[nome]


def ler_arvore_genealogica():
    N = int(input())
    pessoas = {}

    for _ in range(N):
        nome_pai, num_filhos = input().split()
        num_filhos = int(num_filhos)

        pai = obter_pessoa(nome_pai, pessoas)

        for _ in range(num_filhos):
            nome_filho = input()
            filho = obter_pessoa(nome_filho, pessoas)
            pai.adicionar_filho(filho)

    return pessoas


def buscar_e_contar_descendentes(pessoas):
    nome_busca = input()

    if nome_busca in pessoas:
        print(pessoas[nome_busca].contar_descendentes())
    else:
        print("Pessoa não encontrada na árvore genealógica.")


def main():
    pessoas = ler_arvore_genealogica()
    buscar_e_contar_descendentes(pessoas)


if __name__ == "__main__":
    main()