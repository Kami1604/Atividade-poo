#28. Crie um programa que gerencie um estoque de produtos:
#• O usuário deve poder adicionar produtos (nome e quantidade).
#• Permita a busca por um produto específico e exiba sua quantidade.
#• Ofereça a opção de atualizar a quantidade de um produto.
#• Exiba o estoque completo ao final.

estoque = {}

def add():
    nome = input("insira o nome do produto: ").strip().upper()
    quantidade = int(input("insira a quantidade: "))
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"{quantidade} unidades de '{nome}' adicionadas.")

def buscar():
    nome = input("insira o nome do produto a buscar: ").strip().upper()
    if nome in estoque:
        print(f"Produto '{nome}' possui {estoque[nome]} unidades no estoque.")
    else:
        print(f"Produto '{nome}' não encontrado.")

def atualizar_qtd():
    nome = input("insira o nome do produto a atualizar: ").strip().upper()
    if nome in estoque:
        nova_qtd = int(input("Nova quantidade: "))
        estoque[nome] = nova_qtd
        print(f"Quantidade de '{nome}' atualizada para {nova_qtd}.")
    else:
        print(f"Produto '{nome}' não encontrado.")

def exibir_estoque():
    print("\n--- Estoque Completo ---")
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto, qtd in estoque.items():
            print(f"{produto.title()}: {qtd} unidades")

while True:
    print("Menu:")
    print("1 - Adicionar produto")
    print("2 - Buscar produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque completo")
    print("5 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        add()
    elif escolha == "2":
        buscar()
    elif escolha == "3":
        atualizar_qtd()
    elif escolha == "4":
        exibir_estoque()
    elif escolha == "5":
        exibir_estoque()
        print("Encerrado...")
        break
    else:
        print("Opção inválida. Tente novamente.")