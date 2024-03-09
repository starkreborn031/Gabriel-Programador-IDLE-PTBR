# Escreva um programa que faça o "Computador Pensar um numero ramdomicamente" entre 0 e 99 e que peça para o usuario entar descobrir qual foi o numero que o computador escolheu. O programa devera escrever na tela se o usuario acertou ou não o numero.

import random

# Gera um número aleatório entre 0 e 99
numero_aleatorio = random.randint(0, 99)

# Pede para o usuário adivinhar o número
numero_escolhido = int(input("Digite um número entre 0 e 99: "))

# Verifica se o usuário acertou o número
if numero_escolhido == numero_aleatorio:
    print("Você acertou o número!")
else:
    print("Você errou o número!")
    print("O número correto era", numero_aleatorio)
    print("Tente novamente!")

input()

# ______________________________________________________________________________________________________________________________________

# Escreva um programa que leia a velocidade de um carro, se ultrapassar a velocidade de 80km/h ele vai mostrar uma menssagem dizendo que ele foi multado, senão, a multa vai custar R$100 por cada 10km fora do limite, com agravante de 30% caso passe de 110k,/h.

# Leitura da velocidade do carro
velocidade = float(input("Informe a velocidade do carro (km/h): "))
# Definição da velocidade limite
velocidade_limite = 80
# Cálculo da multa
if velocidade <= velocidade_limite:
    print("Tudo certo! Não há multas.")
else:
    # Cálculo da multa base
    excesso_velocidade = velocidade - velocidade_limite
    multa_base = (excesso_velocidade // 10) * 100  # Cálculo da multa por cada 10km/h acima do limite
    # Aplicação do agravante, se necessário
    if velocidade > 110:
        multa_base *= 1.3  # Aumento de 30% na multa

    print(f"Você foi multado! O valor da multa é de R$ {multa_base:.2f}.")

""" Neste programa, o usuário insere a velocidade do carro, e o programa verifica se essa velocidade está acima do limite de 80 km/h. Se estiver, calcula o valor da multa com base em quantos blocos de 10 km/h o carro está acima do limite e aplica um agravante de 30% se a velocidade for maior que 110 km/h. Se a velocidade não estiver acima do limite, o programa informa que não há multa. """

# ______________________________________________________________________________________________________________________________________

def calcular_multa(velocidade):
    if velocidade <= 80:
        return "Você não foi multado."
    else:
        multa_base = (velocidade - 80) // 10 * 100
        if velocidade > 110:
            multa_base *= 1.3
        return f"Você foi multado. O valor da multa é R${multa_base:.2f}."

velocidade = float(input("Digite a velocidade do carro em km/h: "))
print(calcular_multa(velocidade))

"""Este programa pede ao usuário para inserir a velocidade do carro. Se a velocidade for menor ou igual a 80 km/h, o programa informa que o usuário não foi multado. Se a velocidade for maior que 80 km/h, o programa calcula o valor da multa com base na velocidade excedida. Se a velocidade for maior que 110 km/h, um agravante de 30% é aplicado à multa. O valor da multa é então exibido para o usuário. Por favor, note que este é um exemplo simplificado e pode não refletir as regras de trânsito reais. Sempre dirija com segurança e respeite os limites de velocidade. 🚗💨"""

# ______________________________________________________________________________________________________________________________________

# Crie um programa que mostre na tela se o numero digitado pelo usuario é par ou impar se ele é negativo ou positivo se ele é primo ou não primo.

numero = int(input("Digite um número: "))

# Verifica se o número é par ou impar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é impar.")
# Verifica se 
    if numero < 0:
        print("O número é negativo.")
    else:
        print("O número é positivo.")
# Verifica se o número é primo
if numero == 2:
    print("O número é primo.")
elif numero % 2 == 0 or numero % 3 == 0:
    print("O número não é primo.")
else:
    for i in range(5, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")

input()

""" Este programa pede ao usuário para digitar um número e, em seguida, verifica se o número é par ou impar, negativo ou positivo, e primo ou não primo. Se o número for par, o programa imprime "O número é par". Se o número for impar, o programa imprime "O número é impar". Se o número for negativo, o programa imprime "O número é negativo". Se o número for positivo, o programa imprime "O número é positivo". Se o número for primo, o programa imprime "O número é primo". Se o número não for primo, o programa imprime "O número não é primo". """

# ______________________________________________________________________________________________________________________________________


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calcular_imc(peso, altura)

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc < 25:
    print("Você está no peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 35:
    print("Você está com obesidade grau I.")
elif imc >= 35 and imc < 40:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III.")

input()

""" Este programa calcula o IMC (Índice de Massa Corporal) do usuário e, em seguida, informa se o usuário está abaixo do peso ideal, no peso ideal, com sobrepeso, com obesidade grau I, com obesidade grau II ou com obesidade grau III. O IMC é calculado dividindo o peso do usuário em kg pela altura do usuário em metros ao quadrado. """

# ______________________________________________________________________________________________________________________________________

# Crie um programa que desenvolte uma soluçao de distancia de uma viagem em KM. Caucule o preço da passagem, cobrando R$0,50 por km e para viagens até 200km o valor é reduzido á R$0,40. Mas se for maior que 200km passa a ser R$0,60 por km exedido aos 200km.

distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = 200 * 0.50 + (distancia - 200) * 0.60

print(f"O preço da passagem é R$ {preco:.2f}.")

input()

""" Este programa pede ao usuário para digitar a distância da viagem em km e, em seguida, calcula o preço da passagemgem. O preço da passagem é calculado multiplicando a distância da viagem pelo preço por km. Se a distância da viagem for menor ou igual a 200 km, o preço por km é de R$ 0,50. Se a distância da viagem for maior que 200 km, o preço por km é de R$ 0,40 para os primeiros 200 km e R$ 0,60 para cada km excedido aos 200 km. """


def calcular_preco_passagem(distancia):
    # Definição dos preços por km
    preco_ate_200km = 0.40
    preco_acima_200km_base = 0.50  # Para os primeiros 200 km
    preco_acima_200km_excedido = 0.60  # Para km excedidos após 200 km
    # Cálculo do preço da passagem
    if distancia <= 200:
        preco_passagem = distancia * preco_ate_200km
    else:
        # Calcula o preço dos primeiros 200 km e o excedente separadamente
        preco_passagem = 200 * preco_acima_200km_base + (distancia - 200) * preco_acima_200km_excedido

    return preco_passagem
# Leitura da distância da viagem em km
distancia_viagem = float(input("Informe a distância da viagem em km: "))
# Cálculo do preço da passagem
preco_passagem = calcular_preco_passagem(distancia_viagem)
# Exibição do resultado
print(f"O preço da passagem para uma viagem de {distancia_viagem} km é de R$ {preco_passagem:.2f}.")


""" Este programa define uma função calcular_preco_passagem(distancia) que recebe a distância da viagem como argumento e retorna o preço da passagem de acordo com as regras especificadas. Em seguida, o programa lê a distância da viagem fornecida pelo usuário, calcula o preço da passagem usando a função definida e exibe o resultado formatado."""

def calcular_preco_passagem(distancia):
    if distancia <= 200:
        preco = distancia * 0.40
    else:
        preco = 200 * 0.40 + (distancia - 200) * 0.60
    return f"O preço da passagem é R${preco:.2f}."

distancia = float(input("Digite a distância da viagem em km: "))
print(calcular_preco_passagem(distancia))

""" Este programa pede ao usuário para inserir a distância da viagem. Se a distância for menor ou igual a 200 km, o programa calcula o preço da passagem a R$0,40 por km. Se a distância for maior que 200 km, o programa calcula os primeiros 200 km a R$0,40 por km e o restante a R$0,60 por km. O preço da passagem é então exibido para o usuário. Por favor, note que este é um exemplo simplificado e pode não refletir as tarifas reais de viagem. Sempre verifique as tarifas atuais antes de viajar. 🚌💨 """
    
# ______________________________________________________________________________________________________________________________________

# Faça um programa que leia o ano de aniverssario do usuario, e mostre na tela se o ano é bixesto ou não.

ano = int(input("Digite o ano do seu aniversário: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano é bissexto.")
        else:
             print("O ano não é bissexto.")
    else:
        print("O ano é bissexto.")
else:
    print("O ano é bissexto.")

input()

""" Este programa pede ao usuário para digitar o ano do seu aniversário e, em seguida, verifica se o ano é bissexto ou não. Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400 """

def verificar_ano_bissexto(ano):
    # Um ano é bissexto se for divisível por 4, exceto se for divisível por 100,
    # a menos que seja divisível por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
# Leitura do ano de aniversário do usuário
ano_aniversario = int(input("Informe o ano do seu aniversário: "))
# Verificação se o ano é bissexto
if verificar_ano_bissexto(ano_aniversario):
    print(f"O ano {ano_aniversario} é bissexto.")
else:
    print(f"O ano {ano_aniversario} não é bissexto.")

"""Este programa define uma função verificar_ano_bissexto(ano), que recebe um ano como argumento e retorna True se o ano for bissexto, seguindo as regras para anos bissextos. Após isso, o programa solicita ao usuário que informe o ano de seu aniversário, utiliza a função para verificar se este ano é bissexto e exibe o resultado apropriado."""

def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return f"O ano {ano} é bissexto."
    else:
        return f"O ano {ano} não é bissexto."

ano = int(input("Digite o ano do seu aniversário: "))
print(verificar_ano_bissexto(ano))


""" Este programa pede ao usuário para inserir o ano do seu aniversário. Em seguida, verifica se o ano é bissexto ou não. Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400. O resultado é então exibido para o usuário. Por favor, note que este é um exemplo simplificado e pode não refletir todas as regras para determinar anos bissextos. 📅 """

# ______________________________________________________________________________________________________________________________________

# Faça um programa que leia cinco numeros, mostre qual é o maior e qual é o menor entre os 5 numeros digitados pelo usuario na tela.

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número é {maior_numero}.")
print(f"O menor número é {menor_numero}.")

input()

""" Este programa pede ao usuário para digitar cinco números e, em seguida, mostra qual é o maior e qual é o menor entre os números digitados. O programa utiliza as funções max() e min() para encontrar o maior e o menor número, respectivamente. """

print("Digite cinco números:")
# Inicializa as variáveis maximo e minimo com valores None para posterior comparação
maximo = None
minimo = None

for i in range(1, 6):
    numero = float(input(f"Número {i}: "))
    if maximo is None or numero > maximo:
        maximo = numero
    if minimo is None or numero < minimo:
        minimo = numero

print(f"O maior número digitado foi {maximo}.")
print(f"O menor número digitado foi {minimo}.")

""" Neste programa:

-   Solicita-se ao usuário que digite cinco números, um de cada vez.

-   A cada número digitado, o programa compara o número com os valores atualmente armazenados nas variáveis maximo e minimo.

-   Se o número digitado for maior que o valor atual de maximo, ou se maximo ainda não tiver sido definido (None), o programa atualiza maximo com o valor desse número.

-   Se o número digitado for menor que o valor atual de minimo, ou se minimo ainda não tiver sido definido (None), o programa atualiza minimo com o valor desse número.

-   Após todos os cinco números serem lidos e comparados, o programa exibe o maior e o menor número digitado pelo usuário. """


# Inicializa as variáveis para armazenar o maior e o menor número
maior = float('-inf')
menor = float('inf')
# Loop para ler os cinco números
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    # Atualiza o maior e o menor número, se necessário
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
# Mostra o maior e o menor número
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

""" Esse programa solicitará que o usuário insira cinco números e, em seguida, exibirá qual é o maior e qual é o menor número entre os cinco digitados. Espero que isso ajude! """

# Escreva um programa que pergunte o salario de um funcionario e caucule o valor de seu aumento. Para salarios superiores a R$1.300 caucule um aumento de 10%. Para valores inferiores a R$1.300 faça um aumento de 20%.

salario = float(input("Digite o seu salário: "))

if salario > 1300:
    aumento = salario * 0.10
else:
    aumento = salario * 0.20

novo_salario = salario + aumento
print(f"O seu novo salário é de R$ {novo_salario:.2f}.")

input()

""" Este programa pede ao usuário para digitar seu salário e, em seguida, calcula o valor do aumento. Se o salário for maior que R$1.3000, o aumento é de 10%. Se o salário for menor que R$1.3000, o aumento é de 20%. O novo salário é então calculado e exibido na tela. """

# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.

# Leitura dos comprimentos das retas
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))
# Verificação da condição de existência de um triângulo
if (a < b + c) and (b < a + c) and (c < a + b):
    print("As retas podem formar um triângulo!")
else:
    print("As retas não podem formar um triângulo.")

""" Este programa solicita ao usuário que informe o comprimento de três retas. Em seguida, ele verifica se essas retas satisfazem a condição de existência de um triângulo. Se a condição for verdadeira, o programa informa que as retas podem formar um triângulo; caso contrário, informa que as retas não podem formar um triângulo. """
