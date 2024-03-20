# Faça um programa que, Mostre A soma entre todos os numeros Imaperes que sao multiplos de 3 e que se encontram no intervalor de 1 a 500.

for cont in range ( 1, 500 ) :
    print (cont, end= ' ' )

#
    
for cont in range ( 1, 501, 2 ) :

    print (cont, end= ' ' )
    
#

for cont in range ( 1, 501, 2 ) :
    if cont % 3 == 0 :
        print (cont, end= ' ' )


#

soma = 0

for cont in range ( 1, 501, 2 ) :
    if cont % 3 == 0 :
        print ( cont, end= ' ' )
        soma = soma + cont

print ( ' A soma dos valores desejados é de: ' .format ( soma ) )

#

acumulador = 0
soma = 0

for cont in range ( 1, 501, 2 ) :
    if cont % 3 == 0 :
        print ( cont, end= ' ' )
        soma = soma + cont
        acumulador = acumulador + 1 

print ( ' A soma dos valores {} desejados é de: {} ' .format ( soma, acumulador, ) )

#

cont = 0
soma = 0

for numero_1 in range ( 1, 501, 2 ) :
    if numero_1 % 3 == 0 :
        print ( numero_1, end= ' ' )
        soma += numero_1
        cont += 1 

print ( ' A soma dos valores {} desejados é de: {} ' .format ( soma, cont, ) )

#
