# Crie um programa que faça o computador jogar com o usuario: o jogo escolhido é JOKENPO.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('O computador escolheu {}'.format(itens[computador]))

#

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print ('-=' * 20 )
print ('''
       Suas Opções:
       [0] Pedra
       [1] Papel
       [2] Tesoura
       ''')
print ('-=' * 20 )

jogador = int ( input ( ' Qual é a sua Jogada ? ' ) )

print ('-=' * 20 )
print ('Computador escolheu {}' .format ( itens  [computador] ) )
print ('Jogador escolheu {}' .format ( itens [jogador] ) )
print ('-=' * 20 )

#

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print ('-=' * 20 )
print ('''
       Suas Opções:
       [0] Pedra
       [1] Papel
       [2] Tesoura
       ''')
print ('-=' * 20 )
    
jogador = int ( input ( ' Qual é a sua Jogada ? ' ) )

print ('-=' * 20 )
print ('Computador escolheu {}' .format ( itens  [computador] ) )
print ('Jogador escolheu {}' .format ( itens [jogador] ) )
print ('-=' * 20 )

if computador == 0:     #Computador Jogou PEDRA
    
    if jogador == 0:    #Jogador Jogou PEDRA
        print ('Empate!')
    
    elif jogador == 1:  #Jogador Jogou PAPEL
        print ('Jogador Venceu!')
    
    else:               #Jogador Jogou TESOURA
        print ('Computador Venceu!')


elif computador == 1:   #Computador Jogou PAPEL
    
    if jogador == 0:    #Jogador Jogou PEDRA
        print ('O Computador Venceu!')
    
    elif jogador == 1:  #Jogador Jogou PAPEL
        print ('EMPATE!')
    
    else:               #Jogador Jogou TESOURA
        print ('JOGADOR Venceu!')

elif computador == 2:   #Computador Jogou TESOURA
    
    if jogador == 0:    #Jogador Jogou PEDRA
        print ('Jogador Venceu')
    
    elif jogador == 1:  #Jogador Jogou PAPEL
        print ('Jogador Perdeu')
    
    else:               #Jogador Jogou TESOURA
        print ('EMPATE!')

#

from time import sleep  

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print ('-=' * 12 )
print ('''
       Suas Opções:
       [0] Pedra
       [1] Papel
       [2] Tesoura
       ''')
print ('-=' * 12 )
    
jogador = int ( input ( ' Qual é a sua Jogada ? ' ) )

print ('-=' * 12 )

print ('JO')
sleep ( 1 )
print ('KEN')
sleep ( 1 )
print ('PO!!!' ) 

print ('-=' * 12 )

print ('-=' * 12 )
print ('Computador escolheu {}' .format ( itens  [computador] ) )
print ('Jogador escolheu {}' .format ( itens [jogador] ) )
print ('-=' * 12 )

if computador == 0:     #Computador Jogou PEDRA
    
    if jogador == 0:    #Jogador Jogou PEDRA
        print ('Empate!')
    
    elif jogador == 1:  #Jogador Jogou PAPEL
        print ('Jogador Venceu!')
    
    else:               #Jogador Jogou TESOURA
        print ('Computador Venceu!')


elif computador == 1:   #Computador Jogou PAPEL
    
    if jogador == 0:    #Jogador Jogou PEDRA
        print ('O Computador Venceu!')
    
    elif jogador == 1:  #Jogador Jogou PAPEL
        print ('EMPATE!')
    
    else:               #Jogador Jogou TESOURA
        print ('JOGADOR Venceu!')

elif computador == 2:   #Computador Jogou TESOURA
    
    if jogador == 0:    #Jogador Jogou PEDRA
        print ('Jogador Venceu')
    
    elif jogador == 1:  #Jogador Jogou PAPEL
        print ('Jogador Perdeu')
    
    else:               #Jogador Jogou TESOURA
        print ('EMPATE!')

#