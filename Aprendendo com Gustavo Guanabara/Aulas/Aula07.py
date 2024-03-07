
nome = str(input('Qual é seu nome? '))
print('Prazer em Te conhecer: {:=^20}'.format(nome))

#_______________________________________________________________________________________________________________________________________

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
soma = x + y
print('A soma entre {0} e {1} vale {2}'.format(x, y, soma))

#_______________________________________________________________________________________________________________________________________

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
s = x + y
m = x * y
d = x / y
di = x // y
e = x ** y
print('A soma entre {0} e {1} vale {2}'.format(x, y, s))
print('A multiplicação de {0} e {1} vale {2}'.format(x, y, m))
print('A divisão de {0} e {1} vale {2}'.format(x, y, d))
print('A divisão interia de {0} e {1} vale {:.5f}'.format(x, y, di))
print('A exponenciação de {0} e {1} vale {2}'.format(x, y, e))

#_______________________________________________________________________________________________________________________________________

