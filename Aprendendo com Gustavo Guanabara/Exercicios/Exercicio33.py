numero_1 = float(input('Digite o Primeiro numero: '))
numero_2 = float(input('Digite o Segundo numero: '))
numero_3 = float(input('Digite o Terceiro numero: '))

if numero_1 < numero_2 and numero_1 < numero_3:
    menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_2 and numero_3 < numero_1:
    menor = numero_3
print('O Menor valor digitado foi {}'.format(menor))

#
    
numero_1 = float(input('Digite o Primeiro numero: '))
numero_2 = float(input('Digite o Segundo numero: '))
numero_3 = float(input('Digite o Terceiro numero: '))

menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_2 and numero_3 < numero_1:
    menor = numero_3
print('O Menor valor digitado foi {}'.format(menor))

#
    
numero_1 = float(input('Digite o Primeiro numero: '))
numero_2 = float(input('Digite o Segundo numero: '))
numero_3 = float(input('Digite o Terceiro numero: '))
# VERIFICANDO O VALOR MENOR:
menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_2 and numero_3 < numero_1:
    menor = numero_3
# VERIFICANDO O VALOR MAIOR:
maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_2 and numero_3 > numero_1:
    maior = numero_3

print('O Menor valor digitado foi {}'.format(menor))
print('O Maior valor digitado foi {}'.format(maior))

#

