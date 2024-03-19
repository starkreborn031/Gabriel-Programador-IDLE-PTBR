salario = float(input('Digite quanto voce ganha: R$'))
if salario <= 1.250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem Ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(salario , novo))

#

