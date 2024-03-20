# Faça um programa que mostre na tela, Uma contagem regressiva para o estouro de fogos de artificio, Que va de 10 a 0, Com uma pausa de 1 segundo entre eles.

for cont in range ( 0, 11 ) :
    print ( cont )

print ( " acabou ! " )

#

for cont in range ( 10, -1, -1 ) :
    print ( cont )

print ( " E AGORA COMEÇA A FESTA !  ! " )

#

from time import sleep

for cont in range ( 10, -1, -1 ) :
    print ( cont )
sleep ( 1 )

print ( " E AGORA COMEÇA A FESTA !  ! " )

