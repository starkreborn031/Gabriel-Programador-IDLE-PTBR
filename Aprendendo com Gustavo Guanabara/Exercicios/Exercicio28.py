from random import randint

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)

computador = randint(0,5)
jogador = int(input('QUAL NUMERO EU PENSEI? '))

if jogador == computador:
    print('VOCE ACERTOU, O MISERAVÉL E UM GÊNIO!!!')
else:
    print('Infeliz eu pensei no numero {}, voce ERROU KAKAKAKAKA!!!'.format(computador))
    
# ____________________________________________________________________________________________________________________________________________________________________________________________________

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)

computador = randint(0,5)
jogador = int(input('QUAL NUMERO EU PENSEI? '))

print('PROCESSNDO...')
sleep(3)

if jogador == computador:
    print('VOCE ACERTOU, O MISERAVÉL E UM GÊNIO!!!')
else:
    print('Infeliz eu pensei no numero {}, voce ERROU KAKAKAKAKA!!!'.format(computador))

# ____________________________________________________________________________________________________________________________________________________________________________________________________

