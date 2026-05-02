# Exercícios de Programação Orientada a Objetos (Python)

Este repositório reúne implementações de exercícios práticos (EP) sobre conceitos de POO e tópicos relacionados. Abaixo está o que cada arquivo faz e quais ideias ele ilustra.

---

## `EP1_4 - review.py`

**Tema:** revisão procedural — leitura de arquivo, matrizes e tratamento básico de erros.

- **`leiaImagemPBM(filename)`** — Lê um arquivo de imagem no formato PBM (tipo `P1`), valida o cabeçalho, extrai largura e altura e monta uma matriz de pixels (`0`/`1`).
- **`dilata(pixels)`** — Aplica dilatação morfológica: em cada célula, o valor passa a ser o máximo entre o pixel atual e os vizinhos na vizinhança 3×3 (com bordas respeitadas).
- **`PrintMatrix`**, **`ReadFilePbm`**, **`ImageDilation`** — Entrada/saída: lê o nome do arquivo, imprime dimensões e matriz original, depois a matriz dilatada.
- **`main()`** — Usa `try`/`except` para capturar `ValueError` quando o arquivo não é um PBM válido.

Não há classes; o foco é I/O, listas aninhadas e exceções.

---

## `EP2-7 - classes.py`

**Tema:** classes, encapsulamento e composição.

- **`Item`** — Representa um produto com `nome` e `preco`.
- **`CarrinhoDeCompras`** — Mantém uma lista privada `__itens`; permite **`adicionar_item`**, **`calcular_total`** e **`aplicar_desconto(percentual)`** (com validação do percentual entre 0 e 100, senão `ValueError`).
- **`main()`** — Interpreta comandos em texto separados por `;` (`adicionar`, `calcular_total`, `aplicar_desconto`, `criar carrinho`), simulando um carrinho interativo.

---

## `EP3-7 - polimorfismo.py`

**Tema:** classe abstrata, polimorfismo e herança em um mini jogo de batalha.

- **`Personagem(ABC)`** — Classe abstrata com `nome`, `vida` e método abstrato **`atacar(alvo)`**.
- **`Guerreiro`** — Reduz a vida do alvo com **`forcaAtaque`**.
- **`Mago`** — Reduz a vida do alvo com **`poderMagico * 1.5`**.
- **`batalha(p1, p2)`** — Turnos alternados chamando **`atacar`** até uma vida chegar a zero; mensagens de fim de batalha.
- **`criar_personagem`** — Monta `Guerreiro` ou `Mago` a partir de uma linha de entrada (`G` ou outro tipo para mago).

O polimorfismo aparece em **`p1.atacar(p2)`** e **`p2.atacar(p1)`**: o comportamento depende da classe concreta.

---

## `EP3-9 - heranca.py`

**Tema:** herança implícita via composição recursiva — árvore genealógica.

- **`Pessoa`** — Tem `nome` e lista **`filhos`**; **`adicionar_filho`** e **`contar_descendentes`** (conta filhos diretos mais todos os descendentes dos filhos, recursivamente).
- **`obter_pessoa`** — Garante instância única por nome num dicionário (evita duplicar o mesmo nó).
- **`ler_arvore_genealogica`** — Lê `N` relações pai → filhos e monta o grafo em memória.
- **`buscar_e_contar_descendentes`** — Consulta por nome e imprime o total ou mensagem se não existir.

---

## `EP4-6 - interface.py`

**Tema:** protocolo (interface estrutural) e polimorfismo por duck typing.

- **`MetodoPagamento(Protocol)`** — Define o contrato: objeto deve ter **`pagar(self, valor)`**.
- **`CartaoCredito`**, **`Boleto`**, **`Pix`** — Implementam **`pagar`** com mensagens distintas.
- O programa escolhe a implementação por nome (`input`) e imprime o resultado de **`pagar`** para o valor informado.

---

## `EP4-8 - classe abstrata e interface.py`

**Tema:** combinação de ABC (herança “é um”) com `Protocol` (“pode fazer”).

- **`Veiculo(ABC)`** — Atributos `marca` e `preco`; método abstrato **`calcularImposto`**.
- **`Carro`** / **`Moto`** — Impostos 15% e 8% do preço, respectivamente.
- **`Eletrico(Protocol)`** — Contrato **`autonomiaBateria`**.
- **`CarroEletrico`** / **`MotoEletrica`** — Estendem carro/moto e expõem autonomia da bateria.
- **`cria_objeto`** — Fabrica veículo com ou sem autonomia e imprime preço, imposto, total e, se elétrico, autonomia em km.
- **`main()`** — Lê tipo, marca, preco e linha opcional de autonomia (com tratamento de `EOFError`).

---

## `EP5-4 - excecoes multiplas.py`

**Tema:** exceções customizadas e regras de negócio.

- **`SaldoInsuficienteError`**, **`ValorInvalidoError`** — Subclasses de `Exception`.
- **`Conta`** — Saldo interno; **`_ValidarValor`** centraliza regras (valor positivo; saque não pode exceder saldo).
- **`depositar`**, **`sacar`**, **`ver_saldo`** — Operações da conta.
- **`Transacao`** — Encaminha operação (`depositar`/`sacar`) e exibe saldo.
- **`main()`** — Captura **`SaldoInsuficienteError`** e **`ValorInvalidoError`** em um único `except`; outros erros caem em `Exception` genérica.

---

## `EP6-3 - agregacao e heranca.py`

**Tema:** herança abstrata, agregação (funcionário ↔ projetos) e validação.

- **`Funcionario(ABC)`** — `nome`, `salario`, lista **`projetos`**; **`calcular_bonus`** abstrato; **`adicionar_projeto`** aceita `Projeto` ou string e só permite nomes em lista fixa (`Sistema Web`, `BD`, `e-commerce`, `Migração`), senão **`TypeError`**; salário negativo gera **`ValueError`**.
- **`Desenvolvedor`** — Bônus 10% do salário.
- **`Gerente`** — Bônus 20% do salário.
- **`Projeto`** — Agregado simples com **`nome`**.
- **`main()`** — Lê dados separados por `;`, instancia desenvolvedor ou gerente, imprime bônus e, se houver projetos, adiciona e lista.

---

## Como executar

Cada arquivo é um script independente. No diretório deste projeto:

```bash
python "EP1_4 - review.py"
```

(Use aspas nos nomes com espaços, no PowerShell ou cmd.)

A entrada esperada segue o formato de cada `main()` — em geral `input()` no próprio enunciado do exercício.

---

## Ordem sugerida dos tópicos

1. Revisão procedural e exceções — EP1  
2. Classes e encapsulamento — EP2  
3. Abstração, herança e polimorfismo — EP3  
4. Protocolos e ABC — EP4  
5. Exceções múltiplas — EP5  
6. Agregação e modelo de domínio — EP6  
