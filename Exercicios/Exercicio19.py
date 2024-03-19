import random
numero1 = str(input('Qual o nome do Primeiro aluno? '))
numero2 = str(input('Qual o nome do Segundo aluno? '))
numero3 = str(input('Qual o nome do Terceiro aluno? '))
numero4 = str(input('Qual o nome do Quarto aluno? '))
numero5 = str(input('Qual o nome do Quinto aluno? '))
lista = [numero1, numero2, numero3, numero4, numero5]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#_______________________________________________________________________________________________________________________________________________________________

from random import choice
numero1 = str(input('Qual o nome do Primeiro aluno? '))
numero2 = str(input('Qual o nome do Segundo aluno? '))
numero3 = str(input('Qual o nome do Terceiro aluno? '))
numero4 = str(input('Qual o nome do Quarto aluno? '))
numero5 = str(input('Qual o nome do Quinto aluno? '))
lista = [numero1, numero2, numero3, numero4, numero5]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#_______________________________________________________________________________________________________________________________________________________________
