import random
numero_pensado = random.randint (1,20)

numero_digitado = 0
while numero_digitado != numero_pensado:
    numero_digitado = int(input("Adivinhe o numero que estou pensando: "))
    if numero_digitado < numero_pensado:
        print("Muito baixo, tente denovo !")
    elif numero_digitado > numero_pensado:
        print("Muito alto, tente novamente")
    else:
        print("Você acertou, muito bem !")
        break