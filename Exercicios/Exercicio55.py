# Faça um programa que leia o peso e altura de 5 pessoas e no final mostre qual foi o maior peso, a maior altura e o maior IMC.

''' for cont in range ( 1, 10):
        peso_1 = float ( input ( ' Peso da {}ª Pessoa ' .format ( cont ) ) ) '''

#

maior_1 = 0
menor_0 = 0

for cont in range ( 1, 11):
    peso_1 = float ( input ( ' Peso da {}ª Pessoa: ' .format ( cont ) ) )
    
    if cont == 1:
        maior_1 = peso_1
        menor_0 = peso_1
    
    else:
        if peso_1 > maior_1:
            maior_1 = peso_1
        
        if peso_1 < menor_0:
            menor_0 = peso_1

print ( ' \033[032m O Maior \033[0m peso lido foi de {}Kg ' .format ( maior_1 ) )
print ( ' \033[034m O Menor \033[0m peso lido foi de {}Kg ' .format ( menor_0 ) )

