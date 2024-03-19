dias = int(input('Quantos dias o carro ficou alugado?   '))
km = float(input('Quantos Km rodados?   '))
pago = dias * 60
print('O valor a ser pago é de: R${:.2f}'.format(pago))
pago2 = km * 0.50
print('O valor a ser pago por km rodado é de: R${:.2f}'.format(pago2))
total = (pago + pago2)
print('O valor total a ser pago é de: R${:.2f}'.format(total))

# _______________________________________________________________________________________________________________________________________

