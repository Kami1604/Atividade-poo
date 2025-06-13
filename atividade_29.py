#29. Simule um controle de presença para uma aula: Cadastre os nomes dos alunos presentes em uma lista. 
# Exiba o número total de alunos presentes. 
# Pergunte ao usuário se deseja buscar o nome de um aluno específico para verificar se ele estava presente.

alunos = []

def cadastrar(lista, valor):
    lista.append(valor)
    print(f"Quantidade de alunos: {len(lista)}")

def exibir(lista):
    print(f"Quantidade de alunos atual: {len(lista)}")

def buscar(lista, valor):
    if valor in lista:
        print(f"Aluno {valor} presente")
    else:
        print("Aluno não está presente")

while True:
    print("Menu:")
    print("1 - Adicionar aluno a lista de presença")
    print("2 - Visualizar quantidade de alunos")
    print("3 - Buscar aluno")
    print("4 - Encerrar")
    resposta = input("Digite o número correspondente a ação: ")

    if resposta == "1":
        valor = input("Digite o aluno a ser adicionado: ")
        cadastrar(alunos, valor)

    elif resposta == "2":
        exibir(alunos)
        
    elif resposta == "3":
        valor = input("insira o nome do aluno que está buscando: ")
        buscar(alunos, valor)

    elif resposta == "4":
        print(f"Total de alunos presentes: {len(alunos)}")
        print("Encerrando...")
        break
    else:
        print("Resposta inválida")

print(f"Alunos presente {alunos}")
