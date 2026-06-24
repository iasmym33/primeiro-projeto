senha_correta = 123456

for i in range(3):
    senha_digitada = int(input("Digite sua senhas: "))
    if senha_digitada == senha_correta:
        print("Acesso permitido")
        break
    else:
        print("conta bloqueada")