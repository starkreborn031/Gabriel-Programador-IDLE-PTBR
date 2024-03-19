# Desemvolva uma logica que leia o peso e a altura de uma pessoa, caucule o seu IMC e mostre o seu status, de acordo com a tabela: 1= ABAIXO DE 1.85:abaixo do peso. 2 = ENTRE 18.5 E 25:peso ideal. 3 = 26 a 30:sobrepeso. 4 = 31 a 40:obesidade. 5 = ACIMA DE 41:obesidade morbida.

peso = float (input("Digite o seu peso: (Kg)"))
altura = float ('Digite a sua altura: (Metros)')

imc = peso / (altura ** 2)

#

peso = float (input("Digite o seu peso: (Kg)"))
altura = float ('Digite a sua altura: (Metros)')

imc = peso / (altura * altura)

#

peso = float (input("Digite o seu peso: (Kg)"))
altura = float ('Digite a sua altura: (Metros)')

imc = peso / (altura ** 2)

print ('O Seu IMC é de {:.1f}'.format (imc))

#

peso = float (input("Digite o seu peso: (Kg)"))
altura = float ('Digite a sua altura: (Metros)')

imc = peso / (altura ** 2)

print ('O Seu IMC é de {:.1f}'.format (imc))
if imc < 18.5:
    print ('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print ('Peso ideal')
elif imc >= 26 and imc < 30:
    print ('Sobrepeso')
elif imc >= 31 and imc < 40:
    print ('Obesidade')
else:
    print ('Obesidade morbida')

#

peso = float (input("Digite o seu peso: (Kg)"))
altura = float ('Digite a sua altura: (Metros)')

imc = peso / (altura ** 2)

print ('O Seu IMC é de {:.1f}'.format (imc))
if imc < 18.5:
    print ('Abaixo do peso')
elif 18.5 <= imc < 25:
    print ('Peso ideal')
elif 26 <= imc < 30:
    print ('Sobrepeso')
elif 31 <= imc < 40:
    print ('Obesidade')
else:
    print ('Obesidade morbida')
