# Faça um program aque leia: A confederação nacional de natação precisa de um aplicativo que interprete o ano de nascimento de um atleta e mostre a sua categoria de acordo com a sua idade: 1 = ate 9 anos:Mirim. 2 = ate 14 anos:Juvenil. 3 = ate 19 anos:Junior. 4 = ate 20 anos.Senior. 5 = acima de 21 anos:Master.

from datetime import date

atual = date.today().year
nascimento = int(input("Digite o ano de nascimento do atleta: "))

idade = atual - nascimento
print ("O atleta tem", idade, "anos.")

#

atual = date.today().year
nascimento = int(input("Digite o ano de nascimento do atleta: "))

idade = atual - nascimento
print ("O atleta tem {} anos.".format(idade))

#

atual = date.today().year
nascimento = int(input("Digite o ano de nascimento do atleta: "))

idade = atual - nascimento
print ("O atleta tem {} anos.".format(idade))

if idade <= 9:
    print("Categoria: Mirim")
elif idade <= 14:
    print("Categoria: Juvenil")
elif idade <= 19:
    print("Categoria: Junior")
elif idade <= 20:
    print("Categoria: Senior")
else:
    print("Categoria: Master")

#