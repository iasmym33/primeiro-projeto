# Casar ou comprar uma bicicleta ?

print("Casar ou comprar uma bicicleta ?")
resposta = input("Você esta gordo? s/n" )
if resposta == "s":
    quer_emagrecer = input("Você quer emagrecer ?")
    if quer_emagrecer == "s":
        print("Compre uma bicicleta")
    else:
        print("Então case!")
else:
    Quer_engordar = input("Você quer engordar? s/n")
    if Quer_engordar == "s":
            print("Então case!")
    else:
            print("Compre uma bicicleta!")