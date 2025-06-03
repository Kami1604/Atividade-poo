#20. Faça um programa que peça 10 números inteiros, 
#calcule e mostre a quantidade de números pares e a quantidade de números impares.
num_par = 0
num_impar = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    
    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

print(f"\nQuantidade de números pares: {num_par}")  
print(f"Quantidade de números ímpares: {num_impar}") 
