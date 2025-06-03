#15. Crie um programa que receba uma quantidade de numeros definidos pelo usuario e retorne a media dos valores presentes na lista
contador = 0
quantidade = 0

while True:
    soma = int(input("Digite um número "))
    contador += 1
    quantidade = quantidade + soma
    resposta = input("Deseja continuar, se não digite Y ")
    if resposta.upper() != "Y": # se resposta for diferente de Y, ele para. UPPER serve para a letra ficar maiuscula.
        break

print(f" a media dos valores é {quantidade/contador}") # vai apresentar a média dos valor no feito no loop 
