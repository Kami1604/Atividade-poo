#26. Implemente um programa onde o usuário pode: Adicionar itens a uma lista de compras. Exibir todos os itens na lista. 
#Remover um item específico, caso o usuário deseje. Finalizar o programa exibindo a lista final.
lista = []

def cadastrar(lista, valor):
    lista.append(valor)

def excluir(lista, valor):
    if valor in lista:
        lista.remove(valor)
        print(f"carrinho atualizada: {lista}")
    else:
        print("Item não encontrado")

def exibir(lista):
    print("em seu carrinho de compras tem os seguintes itens: ")
    for nome in lista:
        print(f"-{nome}")

while True:
    print("Deseja executar qual ação?")
    print("1 - Adicionar item ao carrinho de compra")
    print("2 - Visualizar carrinho completa")
    print("3 - tirar item do carrinho")
    print("4 - Encerrar")
    resposta = input("Digite o número correspondente a ação: ")
    if resposta == "1":
        valor = input("Qual item vai pro carrinho: ").upper()
        cadastrar(lista, valor)
    elif resposta == "2":
        exibir(lista)
    elif resposta == "3":
        valor = (input("qual item vai remover do carrinho: ").upper())
        excluir(lista, valor)
    elif resposta == "4":
        print("seu carrinho ficou com os seguintes itens")
        for nome in lista:
            print(f"-{nome}")
        print("Encerrando...")
        
        break
    else:
        print("Resposta inválida")