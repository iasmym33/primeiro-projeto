compras = float(input("Qual o valor total da sua? "))

if compras <= 100:
    print(f"Sua compra foi de R${compras} e você não teve desconto")


elif compras >100 and compras <=300:
    desconto = compras * 0.05
    valor_final = compras - desconto
    print(f"Sua compra foi de R$ {compras}. Você teve um desconto de R${desconto}. Sua compra final é de{valor_final}")


elif compras <=500:
    desconto = compras * 0.1
    valor_final = compras - desconto
    print(f"Sua compra foi de R$ {compras}. Você teve um desconto de R${desconto}. Sua compra final é de{valor_final}")

else:
    desconto = compras * 0.15
    valor_final = compras - desconto
    print(f"Sua compra foi de R$ {compras}. Você teve um desconto de R${desconto}. Sua compra final é de{valor_final}")