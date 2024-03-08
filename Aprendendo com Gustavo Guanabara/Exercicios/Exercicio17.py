co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 0.5
print('O comprimento da hipotenusa é', hi)

#_______________________________________________________________________________________________________________________________________________________________

co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa tem comprimento de {hi:.2f}'.format(hi))

#_______________________________________________________________________________________________________________________________________________________________

import math
co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto adjacente: '))
hi = math.hypot(co, ca)
print('A Hipotenusa tem comprimento de {hi:.2f}'.format(hi))

#_______________________________________________________________________________________________________________________________________________________________

from math import hypot
co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto adjacente: '))
hi = hypot(co, ca)
print('A Hipotenusa tem comprimento de {hi:.2f}'.format(hi))

#_______________________________________________________________________________________________________________________________________________________________

