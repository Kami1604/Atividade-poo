#34. Implemente um programa para gerenciar uma agenda de compromissos:
#• O usuário deve poder adicionar compromissos e suas datas.
#• Exiba os compromissos cadastrados.
#• Ofereça a opção de buscar compromissos por data.
#• Exiba todos os compromissos ordenados pela data.

agenda = {}

def adicionar_compromisso():
    data = input("Digite a data do compromisso formato DD/MM/AAAA: ").strip()
    compromisso = input("Digite o compromisso: ").strip()

    if data in agenda:
        agenda[data].append(compromisso)
    else:
        agenda[data] = [compromisso]
    print("Compromisso adicionado com sucesso!")

def exibir_compromissos():
    if not agenda:
        print("Nenhum compromisso cadastrado.")
        return
    print("Compromissos Cadastrados")
    for data in sorted(agenda):
        for comp in agenda[data]:
            print(f"{data}: {comp}")
    print()

def buscar_por_data():
    data = input("Digite a data para buscar formato DD/MM/AAAA: ").strip()
    if data in agenda:
        print(f"Compromissos em {data}:")
        for comp in agenda[data]:
            print(f"- {comp}")
    else:
        print("Nenhum compromisso encontrado nessa data.")
    print()

while True:
    print("Menu")
    print("1 Adicionar compromisso")
    print("2 Exibir todos os compromissos")
    print("3 Buscar compromissos por data")
    print("4 Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_compromisso()
    elif opcao == "2":
        exibir_compromissos()
    elif opcao == "3":
        buscar_por_data()
    elif opcao == "4":
        print("Encerrando agenda")
        break
    else:
        print("Opção inválida. Tente novamente.")