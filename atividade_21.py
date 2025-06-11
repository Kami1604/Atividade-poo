#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input(f"Digite um número inteiro: "))
primo = True

for i in range(2, num -1):
    if num % 2 == 0:
        primo = False
        break
if primo:
    print(f"O número {num} é primo ")
else:
    print(f" O número {num} não é primo ")
