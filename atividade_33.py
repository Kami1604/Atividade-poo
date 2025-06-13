#33. Peça ao usuário para inserir 10 palavras em uma lista.
#• Crie uma nova lista contendo apenas palavras que começam com uma vogal.
#• Exiba a lista original e a filtrada.

palavras = []
palavras_com_vogal = []

for i in range(10):
    palavra = input(f"Digite a {i+1}ª palavra: ").strip()
    palavras.append(palavra)

vogais = ['a', 'e', 'i', 'o', 'u']

for palavra in palavras:
    if palavra and palavra[0].lower() in vogais:
        palavras_com_vogal.append(palavra)

print("Lista original:")
print(palavras)

print("Palavras que começam com vogal:")
print(palavras_com_vogal)