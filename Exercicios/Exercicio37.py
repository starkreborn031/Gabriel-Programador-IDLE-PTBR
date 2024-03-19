# Escrava um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão: 1= para binario 2= Para octal 3= para hexadecimal

numero = int(input('Digite um numero Inteiro: Nº: '))

print = ('''Escolha uma das bases para realiar uma Conversão: 
        [ 1 ] Binario
        [ 2 ] Octal
        [ 3 ] Hexadecimal'']''')

opção = int(input('Sua opção: '))

#

numero = int(input('Digite um numero Inteiro: Nº: '))

print = ('''Escolha uma das bases para realiar uma Conversão: 
        [ 1 ] Binario
        [ 2 ] Octal
        [ 3 ] Hexadecimal'']''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para binario é {}'.format(numero, bin(numero)))
elif opção == 2:
    print('{} convertido para octal é {}'.format(numero, oct(numero)))
elif opção == 3:
    print('{} convertido para hexadecimal é {}'.format(numero, hex(numero)))
else:
    print('Opção invalida. Tente novamente.')

#

numero = int(input('Digite um numero Inteiro: Nº: '))

print = ('''Escolha uma das bases para realiar uma Conversão: 
        [ 1 ] Binario
        [ 2 ] Octal
        [ 3 ] Hexadecimal'']''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para binario é {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida. Tente novamente.')

#

