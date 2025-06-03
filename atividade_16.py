#16. Crie uma função que calcule o fatorial de um numero dado como entrada
# cabecalho 


# variável que salva o valor do fatorial inserido pelo usuário
numero = int (input ("Digite um número inteiro: ")) 

resultado = 1  # essa variável acumula o resultado do fatorial 

for n in  range ( 1 , numero+ 1 ): 
    resultado *= n 

# ira mostrar o resultado 
print ( '\n O resultado de {0}! é: {1}' . format (numero, resultado))

