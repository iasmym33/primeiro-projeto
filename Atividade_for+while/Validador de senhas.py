senha_correta = 123456

for i in range(2,0,-1):
    senha_digitada = int(input("Digite sua senhas: "))
    if senha_digitada == senha_correta:
        print("Acesso permitido")
        break
    else:
        print(f"Senha incorreta, você tem mais {i} tentativas")
else:
        print("conta bloqueada")