#30. Crie um programa que simule um sorteio:
#• Adicione os nomes dos participantes em uma lista.
#• Utilize a função random.choice() para escolher um ganhador aleatório.
#• Exiba o nome do vencedor.

import random
sorteio = []
i = 1

while True:
    pessoa = input(f"insira nome do participante {i} do sorteio: ")
    sorteio.append(pessoa)
    i += 1

    if i > 10:
        break

sorteado = random.choice(sorteio)
print(f"a pessoa sorteada é {sorteado}")