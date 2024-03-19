numero = int(input('Digite um numero de 1 a 9999: '))
num = str(numero)
print('Analisando numero {}...'.format(numero))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

# ____________________________________________________________________________________________________________________________________________________________

numero = int(input('Digite um numero de 1 a 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena  = numero // 100 % 10
milhar = numero // 1000 % 10

print('Analisando numero {}...'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

# ____________________________________________________________________________________________________________________________________________________________
