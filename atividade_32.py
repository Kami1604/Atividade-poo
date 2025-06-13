#32. Peça ao usuário que insira as temperaturas registradas durante uma semana.
#• Exiba a maior e a menor temperatura.
#• Informe a média semanal.
#• Exiba os dias em que a temperatura foi maior que a média.

temperaturas = []
dias_acima_media = []

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / 7

for i in range(7):
    if temperaturas[i] > media:
        dias_acima_media.append(f"Dia {i+1} ({temperaturas[i]}°C)")

print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Média da semana: {media:.1f}°C")

print("Dias com temperatura acima da média:")
if dias_acima_media:
    for dia in dias_acima_media:
        print(dia)
else:
    print("Nenhum dia com temperatura acima da média.")