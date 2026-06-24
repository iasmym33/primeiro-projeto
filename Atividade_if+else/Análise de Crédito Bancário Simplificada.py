salario = float(input("Digite o valor do seu sálario bruto?"))
emprestimo = float(input(" Digite o valor da parcela do empréstimo que deseja pagar"))
porcentagem = salario * 0.30

if emprestimo <= porcentagem:
    print("Crédito Aprovado")
else:
    print("Crédito Recusado")