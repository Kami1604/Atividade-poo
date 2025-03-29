numero1=int(input("Digite um número "))
numero2=int(input("Digite outro número "))
soma=input("Digite uma operação: ")

print("O resultado é ")

if soma == "+":
   print(numero1+numero2 )
elif soma == "-":
   print(numero1-numero2 )
elif soma == "*":
   print(numero1*numero2)
elif soma == "/":
   print(numero1/numero2)
else:
    print("Comando inválido!")