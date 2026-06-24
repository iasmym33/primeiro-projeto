continuar = "s"
while continuar.lower() == "s":
    num = float(input("Digite um numero: "))
    print("TABUADA")

    for i in range (1,11,1):
        print (f"{num} x {i} ={num * i}")
    continuar = input("Quer continuar?")