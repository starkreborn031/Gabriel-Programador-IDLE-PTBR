# Crie um programa que mostre na tela, todos os numeros pares que estao no intervalo entre 1 e 50.

for numero in range ( 0, 51 ) :
    print ( ' {} ' .format ( numero ) )

#
    
for numero in range ( 0, 51 ) :
    print ( numero, end= ' ' )

#

for numero in range ( 0, 51 ) :
    if numero % 2 == 0 :
        print ( numero, end= ' ' )
print (' Acabou ! ! ' )

#

for numero in range ( 2, 51, 2 ) :
    print ( ' . ', end= ' ' )
    print ( numero, end= ' ' )
print (' Acabou ! ! ' )

#

