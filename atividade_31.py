#31. Solicite ao usuário que insira 10 números em uma lista.
#• Exiba os números em ordem crescente.
#• Exiba os números em ordem decrescente.
#• Exiba apenas os valores pares.

numeros = []
pares = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Ordem crescente:")
print(sorted(numeros))

print("Ordem decrescente:")
print(sorted(numeros, reverse=True))

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print("\nNúmeros pares:")
print(pares)