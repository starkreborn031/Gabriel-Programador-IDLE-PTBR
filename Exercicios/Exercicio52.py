# Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero Primo.

numero = int ( input ( 'Digite um Numero para descobrir se ele é ou não Primo. ') )

for cont in range (1, numero + 1 ):
    print (' {} '.format ( cont ), end= '◘' )

#

numero = int ( input ( 'Digite um Numero para descobrir se ele é ou não Primo. ') )

for cont in range (1, numero + 1 ):
    if numero % cont == 0:
        print ( ' \033[34m ', end= '◘' )
    else:
        print ( ' \033[31m ', end= '◘' )
print (' {} '.format ( cont ), end= '◘' )

#

numero = int ( input ( 'Digite um Numero para descobrir se ele é ou não Primo. ') )
total = 0

for cont in range (1, numero + 1 ):
    if numero % cont == 0:
        print ( ' \033[34m ', end= '◘' )
        total += 1
    else:
        print ( ' \033[31m ', end= '◘' )
    print ( ' {} '.format ( cont ), end= '◘' )
print ( ' \n\033[m O numero {} foi divisivel {} vezes. ' .format ( numero, total ) )

#

numero = int ( input ( 'Digite um Numero para descobrir se ele é ou não Primo. ') )
total = 0

for cont in range (1, numero + 1 ):
    if numero % cont == 0:
        print ( ' \033[34m ', end= '◘' )
        total += 1
    else:
        print ( ' \033[31m ', end= '◘' )
    print ( ' {} '.format ( cont ), end= '◘' )

print ( ' \n\033[m O numero {} foi divisivel {} vezes. ' .format ( numero, total ) )
if total == 2:
    print ( ' E por isso ele \033[34m É PRIMO')
else:
    print ( ' E por isso ele \033[31m NÃO É PRIMO ' )