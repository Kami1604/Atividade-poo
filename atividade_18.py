#18. Crie uma função que receba uma lista de numeros como entrada e
# retorne a mesma lista ordenada em ordem crescente

numero = [] # vazio pois o usuário vai inserir os números
print("Insira números inteiros, após terminar digite 'sair' ") 
while True: 
    validacao = input("-")
    if validacao == "sair":
        break
    numero.append(int(validacao)) # adicionando números inseridos pelo usuário 
numero.sort() # utilizado para ordenar a lista de forma crescente 
print(f"os números de formar crescente são: \n{numero}")
