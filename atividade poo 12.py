login_verif= 'Kamily'
senha_verif= 'admin'

login=(input("Digite o seu login "))
senha=(input("Digite sua senha "))

if login_verif == login and senha_verif == senha:
    print("Bem-vindo!")
else:
    print(" Login e senha incorretos!")