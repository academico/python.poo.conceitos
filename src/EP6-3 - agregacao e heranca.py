from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario, projetos=None):
        if salario < 0:
            raise ValueError("Salário inválido")
        self.nome = nome
        self.salario = salario
        self.projetos = projetos if projetos is not None else []

    @abstractmethod
    def calcular_bonus(self):
        pass

    def adicionar_projeto(self, projeto):
        nome_projeto = projeto.nome if isinstance(projeto, Projeto) else projeto
        if nome_projeto not in ["Sistema Web", "BD", "e-commerce", "Migração"]:
            raise TypeError("Projeto com nome inválido")
        else:
            self.projetos.append(nome_projeto)


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, projetos=None):
        super().__init__(nome, salario, projetos)

    def calcular_bonus(self):
        return self.salario * 0.1


class Gerente(Funcionario):
    def __init__(self, nome, salario, projetos=None):
        super().__init__(nome, salario, projetos)

    def calcular_bonus(self):
        return self.salario * 0.2


class Projeto:
    def __init__(self, nome):
        self.nome = nome


def main():
    try:
        nome, salario, funcao = input().split("; ")
        projetos = input().split("; ")

        if funcao.lower() == "desenvolvedor":
            funcionario = Desenvolvedor(nome, int(salario))
            print("Desenvolvedor criado")
        else:
            funcionario = Gerente(nome, int(salario))
            print("Gerente criado")

        print(f"Bonus: {funcionario.calcular_bonus()}")

        if len(projetos) != 0:
            for p in projetos:
                projeto = Projeto(p.strip())
                funcionario.adicionar_projeto(projeto)
            print(f"Projetos: {funcionario.projetos}")

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
