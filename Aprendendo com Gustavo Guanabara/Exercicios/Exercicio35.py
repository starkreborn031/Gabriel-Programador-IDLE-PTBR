reta_1 = float(input('Digite a reta 1: '))
reta_2 = float(input('Digite a reta 2: '))
reta_3 = float(input('Digite a reta 3: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_3 + reta_1 and reta_3 < reta_2 + reta_1:
    print('Os Seguimentos acima PODEM FORMAR UM TRIANGULO!')
else:
    print('Os Seguimentos acima NÃO PODEM FORMAR UM TRIANGULO!')

#

