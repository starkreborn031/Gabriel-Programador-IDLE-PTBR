# Desenvolva um programa que, Leia seia numeros inteiros e mostre a soma aoenas daqueles que forem pares. se o valor digitado for impar DESCONSIDERE-O.

numero_1 = int ( input ( ' Digite um numero de 1 a 99: ') )

#

for cont in range ( 1, 6): 
    numero_1 = int ( input ( ' Digite um numero de 1 a 99: ') )

#

soma = 0
cont = 0

for cont in range ( 1, 6): 
    numero_1 = int ( input ( ' Digite o {} valor: ' .format ( cont ) ) )
    soma = soma + numero_1
    cont = cont + 1

print ( ' Voce informou {} numero e a soma foi {}. ' .format ( cont, soma ) )

#

soma = 0
cont = 0

for cont in range ( 1, 6): 
    numero_1 = int ( input ( ' Digite o {} valor: ' .format ( cont ) ) )
    if numero_1 % 2 == 0:
        soma = soma + numero_1
        cont = cont + 1

print ( ' Voce informou {} numero e a soma foi {}. ' .format ( cont, soma ) )

