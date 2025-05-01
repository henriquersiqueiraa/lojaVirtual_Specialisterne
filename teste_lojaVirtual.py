# Loja Virtual Simples em Python (Controle de Clientes, Produtos, Carrinho e Vendas)

import datetime


# -------------------- MODELOS --------------------
class Cliente:
    def __init__(self, id, nome, cpf, email, endereco, telefone):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        self.telefone = telefone


class Produto:
    def __init__(self, id, nome, categoria, preco, estoque):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque


class Venda:
    def __init__(self, id_venda, cliente, itens, data):
        self.id_venda = id_venda
        self.cliente = cliente
        self.itens = itens  # lista de tuplas (produto, quantidade)
        self.data = data

    def total(self):
        return sum(produto.preco * quantidade for produto, quantidade in self.itens)


# -------------------- BANCO DE DADOS EM MEMÓRIA --------------------
clientes = []
produtos = []
vendas = []
carrinho = []


# -------------------- FUNÇÕES --------------------
def cadastrar_cliente():
    id = len(clientes) + 1
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    cliente = Cliente(id, nome, cpf, email, endereco, telefone)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")


def cadastrar_produto():
    id = len(produtos) + 1
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    estoque = int(input("Quantidade em estoque: "))
    produto = Produto(id, nome, categoria, preco, estoque)
    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")


def listar_produtos():
    for p in produtos:
        print(f"{p.id} - {p.nome} | R$ {p.preco:.2f} | Estoque: {p.estoque}")


def adicionar_ao_carrinho():
    listar_produtos()
    id_prod = int(input("Digite o ID do produto: "))
    quantidade = int(input("Quantidade: "))
    produto = next((p for p in produtos if p.id == id_prod), None)
    if produto and produto.estoque >= quantidade:
        carrinho.append((produto, quantidade))
        print("Produto adicionado ao carrinho!\n")
    else:
        print("Produto não encontrado ou estoque insuficiente.\n")


def finalizar_venda():
    if not carrinho:
        print("Carrinho vazio.\n")
        return

    print("Clientes cadastrados:")
    for c in clientes:
        print(f"{c.id} - {c.nome}")

    id_cliente = int(input("Digite o ID do cliente: "))
    cliente = next((c for c in clientes if c.id == id_cliente), None)

    if not cliente:
        print("Cliente não encontrado.\n")
        return

    for produto, qtd in carrinho:
        produto.estoque -= qtd

    venda = Venda(len(vendas) + 1, cliente, carrinho.copy(), datetime.datetime.now())
    vendas.append(venda)
    carrinho.clear()
    print(f"Venda finalizada! Total: R$ {venda.total():.2f}\n")


def relatorio_vendas():
    print("\n--- RELATÓRIO DE VENDAS ---")
    for v in vendas:
        print(f"Venda ID: {v.id_venda} | Cliente: {v.cliente.nome} | Data: {v.data.strftime('%d/%m/%Y %H:%M')}")
        for produto, qtd in v.itens:
            print(f"  - {produto.nome} x{qtd} = R$ {produto.preco * qtd:.2f}")
        print(f"Total: R$ {v.total():.2f}\n")


# -------------------- MENU PRINCIPAL --------------------
def menu():
    while True:
        print("""
--- MENU LOJA VIRTUAL ---
1. Cadastrar cliente
2. Cadastrar produto
3. Adicionar ao carrinho
4. Finalizar venda
5. Relatório de vendas
6. Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            adicionar_ao_carrinho()
        elif opcao == "4":
            finalizar_venda()
        elif opcao == "5":
            relatorio_vendas()
        elif opcao == "6":
            break
        else:
            print("Opção inválida!\n")


# Executar o menu
menu()