#27. Peça ao usuário para inserir as notas de um aluno em uma lista. Após cadastrar todas as notas, calcule e exiba:
#• A maior nota.
#• A menor nota.
#• A média das notas.

notas = []

quantidade = int(input("Quantas notas deseja cadastrar? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)


maior = notas[0]
menor = notas[0]
soma = 0

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    soma += nota

media = soma / len(notas)

print(f"Maior nota: {maior:.1f}")
print(f"Menor nota: {menor:.1f}")
print(f"Média das notas: {media:.1f}")