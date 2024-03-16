# Escrava um programa que leia 2 numeros inteiros e compare-os, mostrando na tela uma mensagem: 1 = O primeiro valor é maior. 2 = o segundo valor é maior. 3 = Não existe valor maior, os dois são iguais.

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

if numero_1 > numero_2:
    print('O primeiro valor é maior.')
else: numero_2 > numero_1

print ('O segundo valor é maior.')

#

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

if numero_1 > numero_2:
    print('O PRIMEIRO valor é maior.')
elif numero_2 > numero_1:
    print ('O SEGUNDO valor é maior.')
elif numero_1 == numero_2:
    print ('Não existe valor maior, os dois são iguais.')

#

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

if numero_1 > numero_2:
    print('O PRIMEIRO valor é maior.')
elif numero_2 > numero_1:
    print ('O SEGUNDO valor é maior.')
else: 
    print ('Não existe valor MAIOR, os dois são IGUAIS.')
