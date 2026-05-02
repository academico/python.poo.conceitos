class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoDeCompras:
    def __init__(self): 
        self.__itens = []  # lista inicialmente vazia

    def adicionar_item(self, item):
        self.__itens.append(item)

    def calcular_total(self):  # retorna o preço total de todos os itens
        total = 0
        for i in self.__itens:
            total += i.preco
        return total

    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            total = self.calcular_total()
            novo_total = total * (1 - percentual / 100)
            return novo_total
        else:
            raise ValueError("Percentual de desconto inválido.")
    

def main():
    carrinho = CarrinhoDeCompras()
    comandos = input().split(';')
    for comando in comandos:
        comando = comando.strip().lower()
        
        if not comando:  # ignora vazio
            continue
        
        if comando.startswith('adicionar'):
            partes = comando.replace("adicionar ", "").split(',')
            nome = partes[0].strip()
            preco = float(partes[1].strip())
            item = Item(nome, preco)
            carrinho.adicionar_item(item)
            
        elif comando.startswith('calcular_total'):
            print(f"{carrinho.calcular_total():.1f}")
            
        elif comando.startswith('aplicar_desconto'):
            try:
                partes = comando.split()
                percentual = float(partes[1])
                print(f"{carrinho.aplicar_desconto(percentual):.1f}")
            except (ValueError, IndexError) as e:
                print("Erro ao aplicar desconto:", e)
                
        elif comando.startswith('criar carrinho'):
            carrinho = CarrinhoDeCompras()  # reinicia o carrinho

if __name__ == "__main__":
    main()
