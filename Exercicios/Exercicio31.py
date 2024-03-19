distancia = float(input('Qual é a distancia da viagem que voce deseja ralizar? '))
print('Voce esta prestes a começar uma viagem de {}Km!')

#

distancia = float(input('Qual é a distancia da viagem que voce deseja ralizar? '))
print('Voce esta prestes a começar uma viagem de {}Km!')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(distancia))

#

distancia = float(input('Qual é a distancia da viagem que voce deseja ralizar? '))
print('Voce esta prestes a começar uma viagem de {}Km!')
""" if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45 """
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(distancia))

#