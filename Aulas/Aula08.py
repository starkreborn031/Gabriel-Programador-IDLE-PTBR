import math

numero = int(input('Digite um numero de 1 á 9: '))
raiz = math.sqrt(numero)
print('A raiz de {} é igual a {:.2f}'.format(numero, raiz))

#_______________________________________________________________________________________________________________________________________

numero = int(input('Digite um numero de 1 á 9: '))
raiz = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, math.ceil(raiz)))

#_______________________________________________________________________________________________________________________________________

numero = int(input('Digite um numero de 1 á 9: '))
raiz = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, math.floor(raiz)))

#_______________________________________________________________________________________________________________________________________

from math import sqrt, floor, ceil
 
numero = int(input('Digite um numero de 1 á 9: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {:.2f}'.format(numero, raiz))

#_______________________________________________________________________________________________________________________________________

numero = int(input('Digite um numero de 1 á 9: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {:.2f}'.format(numero, floor(raiz)))

#_______________________________________________________________________________________________________________________________________

numero = int(input('Digite um numero de 1 á 9: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {:.2f}'.format(numero, ceil(raiz)))

#_______________________________________________________________________________________________________________________________________

import random
numero = random.randint(1, 10)
print(numero)

#_______________________________________________________________________________________________________________________________________

import emoji
print(emoji.emojize('Olá, mundo! \U0001f60a:', language='pt'))
print(emoji.emojize('Olá, mundo! :grinning_face:', language='pt'))

#_______________________________________________________________________________________________________________________________________

import emoji
print(emoji.emojize('Olá, mundo! :earth_americas:', use_aliases=True))

#_______________________________________________________________________________________________________________________________________

