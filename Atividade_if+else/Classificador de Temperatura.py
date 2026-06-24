temperatura = int(input("Qual a temperatura atua da sua cidade? "))

if temperatura<15:
    print("O clima está frio")
elif temperatura >15 and temperatura<25:
    print("O clima está agradável")
else:
    print("o clima esta quente")
