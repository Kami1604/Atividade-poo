#17. Desenvolva uma função que receba um palavra como entrada e retorne a quantidade de vogais presentes na palavra

palavra = str(input("Digite um Palavra "))

vogal = "aeiou"
palavra = palavra.lower()

i = 0
for letras in palavra:
    if letras in vogal:
        i+=1
        
print (f" A quantidade de vogal é {i}") 
   