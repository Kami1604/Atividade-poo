#19. Uma pessoa deseja otimizar a sua lista de compras para isso criar 
# um algoritmo que permita a inclusão dos itens faltantes em uma lista
lista = ["Abobrinha", "Maçã", "Café"]
print("Deseja adicionar mais algum item a sua lista?")
print("Caso não queria adicionar mais nada. Digite sair")

while True:
    produto = input("Adicionar produto: ")
    if produto == "sair":
        break 
    lista.append(produto) 
    
for produto in lista:
    print(produto)
    
