class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class ValorInvalidoError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Conta:
    def __init__(self, valor):
        self._ValidarValor(valor, "depositar")
        self._saldo = valor

    def _ValidarValor(self, valor, transacao="none"): 
        if valor <= 0:
            raise ValorInvalidoError("Erro: Valor deve ser positivo")
        if transacao == "sacar" and self._saldo < valor:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente")

    def depositar(self, valor):
        self._ValidarValor(valor, "depositar")
        self._saldo += valor

    def sacar(self, valor):
        self._ValidarValor(valor, "sacar")
        self._saldo -= valor

    def ver_saldo(self):
        print(f"Saldo atual: R$ {self._saldo:.2f}")


def Transacao(conta, operacao, valor):
    if operacao == "depositar":
        conta.depositar(valor)
        conta.ver_saldo()
    elif operacao == "sacar":
        conta.sacar(valor)
        conta.ver_saldo()
    else:
        print("Por favor, digite uma operação válida")


def main():
    try:
        saldo_inicial = float(input().strip())
        conta = Conta(saldo_inicial)

        entrada = input().strip().split()
        operacao = entrada[0].lower()
        valor_op = float(entrada[1])

        Transacao(conta, operacao, valor_op)

    except (SaldoInsuficienteError, ValorInvalidoError) as e:
        print(e)
    except Exception as e:
        print("Erro inesperado:", e)


if __name__ == "__main__":
    main()
