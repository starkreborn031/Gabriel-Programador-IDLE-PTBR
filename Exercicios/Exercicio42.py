# Crie um progra que faça a soma de 3 valores que o usuario ia digitar e mostre na tela se é possivel formar um triangulo, se sim, que ele mostre qual é o tipo de triangulo que vai se formar: 1 = EQUILATERO:todos os lados iguais. 2 = ISOSCELES:dois lados iguais. 3 = ESCALENO:todos os lados diferentes. 4 = NÃO FORMA TRIANGULO NENHUM.

reta_1 = float(input('Digite a reta 1: '))
reta_2 = float(input('Digite a reta 2: '))
reta_3 = float(input('Digite a reta 3: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_3 + reta_1 and reta_3 < reta_2 + reta_1:
    print('Os Seguimentos acima PODEM FORMAR UM TRIANGULO!')

    if reta_1 == reta_2 and reta_2 == reta_3:
        print('TRIANGULO EQUILATERO:todos os lados iguais.')

else:
    print('Os Seguimentos acima NÃO PODEM FORMAR UM TRIANGULO!')

#

reta_1 = float(input('Digite a reta 1: '))
reta_2 = float(input('Digite a reta 2: '))
reta_3 = float(input('Digite a reta 3: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_3 + reta_1 and reta_3 < reta_2 + reta_1:
    print('Os Seguimentos acima PODEM FORMAR UM TRIANGULO!', end=' ')

    if reta_1 == reta_2 and reta_2 == reta_3:
        print('TRIANGULO EQUILATERO:todos os lados iguais.')

else:
    print('Os Seguimentos acima NÃO PODEM FORMAR UM TRIANGULO!')

#

reta_1 = float(input('Digite a reta 1: '))
reta_2 = float(input('Digite a reta 2: '))
reta_3 = float(input('Digite a reta 3: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_3 + reta_1 and reta_3 < reta_2 + reta_1:
    print('Os Seguimentos acima PODEM FORMAR UM TRIANGULO!', end=' ')

    if reta_1 == reta_2 and reta_2 == reta_3:
        print('TRIANGULO EQUILATERO:todos os lados iguais.')
    
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print('TRIANGULO ISOSCELES:dois lados iguais.')
    
    elif reta_1 != reta_2 and reta_1 != reta_3 and reta_2 != reta_3:
        print('TRIANGULO ESCALENO:todos os lados diferentes.')

else:
    print('Os Seguimentos acima NÃO PODEM FORMAR UM TRIANGULO!')

#
   
reta_1 = float(input('Digite a reta 1: '))
reta_2 = float(input('Digite a reta 2: '))
reta_3 = float(input('Digite a reta 3: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_3 + reta_1 and reta_3 < reta_2 + reta_1:
    print('Os Seguimentos acima PODEM FORMAR UM TRIANGULO!', end=' ')

    if reta_1 == reta_2 and reta_2 == reta_3:
        print('TRIANGULO EQUILATERO:todos os lados iguais.')
    
    elif reta_1 != reta_2 and reta_1 != reta_3 or reta_2 != reta_3:
        print('TRIANGULO ISOSCELES:dois lados iguais.')
    
    else:
        print('TRIANGULO ESCALENO:todos os lados diferentes.')

else:
    print('Os Seguimentos acima NÃO PODEM FORMAR UM TRIANGULO!')

#
   
