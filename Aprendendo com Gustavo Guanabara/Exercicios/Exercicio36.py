# Escrava um programa para aprovar um emprestimo bancario para a acompra de uma casa. o programa par vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Caucule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do seu salario: R$"))
anos = int(input("Digite em quantos anos voce vai pagar: "))

prestacao = casa / (anos * 12)

print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print ('A prestação mensal sera de R${:.2f}'.format(prestacao))

#

casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do seu salario: R$"))
anos = int(input("Digite em quantos anos voce vai pagar: "))

minimo = salario * 30 / 100
prestacao = casa / (anos * 12)

print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print ('A prestação mensal sera de R${:.2f}'.format(prestacao))
print ('Comparando com o minimo de R${:.2f} permitido'.format(minimo))

#

casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do seu salario: R$"))
anos = int(input("Digite em quantos anos voce vai pagar: "))

minimo = salario * 30 / 100
prestacao = casa / (anos * 12)

print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print ('A prestação mensal sera de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print ('Emprestimo aprovado!')
else:
    print ('Emprestimo negado!')

#

