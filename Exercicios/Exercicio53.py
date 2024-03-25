# Crie um programa que, leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

frase_1 = str ( input ( ' Digite uma frase: ' ) )
print ( ' Voce digitou a frase {}. ' .format ( frase_1 ) )

#

frase_1 = str ( input ( ' Digite uma frase: ' ) )
palavras = frase_1.split()
junto = '' .join ( palavras )

print ( ' Voce digitou a frase {}. ' .format ( frase_1 ) )

#

frase_1 = str ( input ( ' Digite uma frase: ' ) )
palavras = frase_1.split()
junto = '' .join ( palavras )
inverso = ''

for letra in range ( len ( junto ) -1, -1, -1):
    inverso += junto [letra]
print ( junto, inverso)

#

frase_1 = str ( input ( ' Digite uma frase: ' ) )
palavras = frase_1.split()
junto = '' .join ( palavras )
inverso = ''

for letra in range ( len ( junto ) -1, -1, -1):
    inverso += junto [letra]
print ( junto, inverso)

#

frase_1 = str ( input ( ' Digite uma frase: ' ) ) .split () .upper ()
palavras = frase_1 .split ()
junto = '' .join ( palavras )
inverso = ''

for letra in range ( len ( junto ) -1, -1, -1):
    inverso += junto [letra]
if inverso == junto:
    print ( ' A frase digitada \033[34m É PALINDROMO! \033[0m' )
else:
    print ( ' A frase digitada \033[31m NÃO É UM PALINDROMO \033[0m' )

#

frase_1 = str ( input ( ' Digite uma frase: ' ) ) .strip().upper()

palavras = frase_1.split()

junto = ''.join ( palavras )

inverso = ''

for letra in range ( len ( junto ) -1, -1, -1):
    inverso += junto [letra]

print ( ' O Inverso de {} é {}. ' .format ( junto, inverso ) )

if inverso == junto:
    print ( ' A frase digitada \033[34m É PALINDROMO! \033[0m' )

else:
    print ( ' A frase digitada \033[31m NÃO É UM PALINDROMO \033[0m' )

#

frase_1 = str ( input ( ' Digite uma frase: ' ) ) .strip().upper()

palavras = frase_1.split()

junto = ''.join ( palavras )

inverso = junto [ : : -1 ] 

print ( ' O Inverso de {} é {}. ' .format ( junto, inverso ) )

if inverso == junto:
    print ( ' A frase digitada \033[34m É PALINDROMO! \033[0m' )

else:
    print ( ' A frase digitada \033[31m NÃO É UM PALINDROMO \033[0m' )
