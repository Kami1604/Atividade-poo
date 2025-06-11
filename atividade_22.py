#22. Crie um programa que simule o acesso a um sistema onde o usuário tem três tentativas para informar a senha correta.
usuar_valido = "Kamily"
senha_valida = "kam123"
contador = 0

while True:
    usuar = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    
    if usuar == usuar_valido and senha == senha_valida:
        print("Bem - vindo ao sistema!")
    else:
        print("Usuário ou senha inválida.")
        contador += 1
        if contador == 3:
            print("Tentativas exedidas.")
            break
            