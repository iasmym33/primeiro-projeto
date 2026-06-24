print("Digite o comprimento de três retas (A, B e C)")
A1= int(input("Digite o comprimento da primeira reta: "))
B1= int(input("Digite o comprimento da segunda reta: "))
C1= int(input("Digite o comprimento da terceira reta: "))


if A1+B1 <C1 or B1+C1 <A1 or A1+C1 <B1 :
    print("Essas medidas não formam um triângulo")

elif A1 == B1  and A1 == C1 and B1 == C1:
    print("Este triângulo é Equilátero")
elif A1 == B1  or A1 == C1 or B1 == C1:
    print("Este triângulo é Isósceles")
elif A1 != B1  and A1 != C1 and B1 != C1:
    print("Este triângulo é Escaleno")