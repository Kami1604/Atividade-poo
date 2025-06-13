#25. Crie um programa que permita ao usuário cadastrar nomes de alunos em uma lista. Depois, exiba todos os alunos cadastrados.
# Pergunte ao usuário se deseja remover um aluno específico. Exiba a lista atualizada após a remoção.
lista = []

def cadastrar(lista, valor):
    lista.append(valor)

def excluir(lista, valor):
    if valor in lista:
        lista.remove(valor)
        print(f"lista atualizada: {lista}")
    else:
        print("Item não encontrado")

def exibir(lista):
    print("na lista atualmente temos: ")
    for nome in lista:
        print(f"-{nome}")

while True:
    print("Deseja executar qual ação?")
    print("1 - Adicionar item a lista")
    print("2 - Visualizar lista completa")
    print("3 - Excluir item")
    print("4 - Encerrar")
    resposta = input("Digite o número correspondente a ação: ")
    if resposta == "1":
        valor = input("Insira o nome do novo aluno a ser adicionado: ").upper()
        cadastrar(lista, valor)
    elif resposta == "2":
        exibir(lista)
    elif resposta == "3":
        valor = (input("Insira o nome do aluno a excluir da lista: ").upper())
        excluir(lista, valor)
    elif resposta == "4":
        print("Encerrando...")
        break
    else:
        print("Resposta inválida")