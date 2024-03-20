# Estrutura de Repetição FOR 
# É nescessario ter PROFISSIENCIA para utilizar a funçao FOR:

for numero in range(1, 11):
    print(numero)

for numero in range(1, 11, 2):
    print(numero)

#

for numero in range(10, 0, -1):
    print(numero)
    if numero == 5:
        break
    else:
        continue

for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)
    else:
        continue
    break
else:
    print("Acabou!")

#
    
i = int ( input ( ' Incio: ') )
f = int ( input ( ' Fim: ' ) )
p = int ( input ( ' Passo: ') )

for c in range (i, f+1, p):
    print(c)
else:
    print('Acabou!')

#
    
s = 0

for c in range ( 0, 5 ): 
    numero = int ( input ( ' Numero: ' ) )
    s = s + numero

print('Soma dos valores a cima é: ', s)

#

