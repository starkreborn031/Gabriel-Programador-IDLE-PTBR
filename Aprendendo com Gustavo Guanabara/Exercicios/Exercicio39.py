# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 1 = se ele ainda vai se alistar no exercito militar. 2 = se é a hora de se alistar. 3 = se ja do tempo do alistamento. O programa tbm deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nascimento = int(input('Em que ano voce nasceu: '))
idade = atual - nascimento

print ('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
 
#

atual = date.today().year
nascimento = int(input('Em que ano voce nasceu: '))
idade = atual - nascimento

print ('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade == 18:
    print ('Voce tem que se alistar Imediatamente')

elif idade < 18:
    print ('Ainda falta {} anos para o seu alistamento'.format(18 - idade))

else: idade > 18
print ('Ja passou {} anos do seu alistamento'.format(idade - 18))

#

atual = date.today().year
nascimento = int(input('Em que ano voce nasceu: '))
idade = atual - nascimento

print ('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade == 18:
    print ('Voce tem que se alistar Imediatamente')

elif idade < 18:
    saldo = 18 - idade
    print ('Ainda falta {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print ('seu alistamento sera em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print ('Ja passou {} anos do seu alistamento'.format(saldo))
    ano = atual - saldo
    print ('Seu alistamento foi em {}'.format(ano))

#

atual = date.today().year
nascimento = int(input('Em que ano voce nasceu: '))
sexo = input("Qual é o seu sexo? (feminino/masculino): ")

if sexo.lower() == 'feminino':
    print("Você não precisa se alistar no exército.")
else:
    # Aqui você pode continuar com o restante do seu programa para pessoas do sexo masculino
    print("Você precisa se alistar no exército.")

idade = atual - nascimento

print ('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade == 18:
    print ('Voce tem que se alistar Imediatamente')

elif idade < 18:
    saldo = 18 - idade
    print ('Ainda falta {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print ('seu alistamento sera em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print ('Ja passou {} anos do seu alistamento'.format(saldo))
    ano = atual - saldo
    print ('Seu alistamento foi em {}'.format(ano))

#