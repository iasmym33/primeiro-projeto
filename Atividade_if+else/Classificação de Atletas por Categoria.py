idade = int(input("Qual a sua idade?"))

if idade <= 9:
    print("Categoria Mirin")
elif idade <=14:
    print("Categoria Infantil")
elif idade <= 19:
    print("Categoria Junior")
else:
    print("Categoria Sênior")