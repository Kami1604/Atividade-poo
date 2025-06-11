#23. Escreva um programa que pergunte o valor total da conta e permita ao usuário escolher 
# a porcentagem de gorjeta que deseja adicionar (10%, 15%, ou 20%).
conta = float(input("Digite o valor total da conta: "))

print("Escolha a porcentagem da gorjeta: ")
print("1 - 10%")
print("2 - 15%")
print("3 - 20%")
escolha = input("Escolha a opção 1, 2 ou 3: ")
if escolha == "1":
    porcentagem = 0.10
elif escolha == "2":
    porcentagem = 0.15
elif escolha == "3":
    porcentagem = 0.20
else:
    print("Escolha inválida, o valor da conta não se aplica a gorjeta!")
    porcentagem = 0.0
gorjeta = conta * porcentagem
valor = conta + gorjeta

print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Valo a ser pago: R${valor:.2f}")
