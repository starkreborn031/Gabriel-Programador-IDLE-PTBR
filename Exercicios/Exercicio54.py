# Crei um programa que leia o ano de nascimento de 10 pessoas. No final, mostre quantas pessoas ainda nao atingiram a maior idade e quantas ja são maiores.

from datetime import date

ano_atual = date .today() .year

nascimento_1 = int ( input ( ' Em em que a pessoa [1] nasceu? ' ) )
idade_1 = ano_atual - nascimento_1

print ( ' Essa Pessoa tem  {} anos' .format ( idade_1 ) )

#

ano_atual = date .today() .year

nascimento_1 = int ( input ( ' Em em que a pessoa [1] nasceu? ' ) )
idade_1 = ano_atual - nascimento_1

if idade_1 >= 21:
    print ( ' Essa pessoa \033[032m É MAIOR DE IDADE')
else:
    print ( ' Essa pessoa \033[031m É MENOR DE IDADE. ')

#
    
ano_atual = date .today() .year

for pessoas_0 in range ( 1, 11):

    nascimento_1 = int ( input ( ' Em em que a pessoa [1] nasceu? ' ) )
    idade_1 = ano_atual - nascimento_1

    if idade_1 >= 21:
        print ( ' Essa pessoa \033[032m É MAIOR DE IDADE')
    else:
        print ( ' Essa pessoa \033[031m É MENOR DE IDADE. ')

#

ano_atual = date .today() .year

total_maior = 0
total_menor = 0

for pessoas_0 in range ( 1, 11):

    nascimento_1 = int ( input ( ' Em em que a pessoa {}ª nasceu? ' .format (pessoas_0) ) )
    idade_1 = ano_atual - nascimento_1

    if idade_1 >= 21:
        total_maior += 1
        '''print ( ' Essa pessoa \033[032m É MAIOR DE IDADE')'''
    else:
        total_menor += 1
        '''print ( ' Essa pessoa \033[031m É MENOR DE IDADE. ')'''

print ( ' Ao finlizar a nossa pesquisa, contamos {} de interações com \033[032m MAIORES DE IDADE \033[0m ' .format ( total_maior ) )
print ( ' Ao finlizar a nossa pesquisa, contamos {} de interações com \033[031m MENORES DE IDADE \033[0m' .format ( total_menor ) )
