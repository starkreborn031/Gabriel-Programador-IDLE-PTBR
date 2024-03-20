# Faça um programa que mostre na tela, Uma contagem regressiva para o estouro de fogos de artificio, Que va de 10 a 0, Com uma pausa de 1 segundo entre eles.

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("Estourou!")

#

import time

                                    # Função para a contagem regressiva
def contagem_regressiva(tempo):
    for i in range(tempo, -1, -1):  # Começa em 'tempo' e vai até 0 (inclusive) com passo -1
        print(i)
        time.sleep(1)               # Pausa de 1 segundo

                                    # Chamando a função com o tempo desejado
contagem_regressiva(10)
print("Estourou!")

#

# Crie um programa que mostre na tela, todos os numeros pares que estao no intervalo entre 1 e 50.

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#

# Loop de 1 a 50
for numero in range(1, 51):
    if numero % 2 == 0:             # Verifica se o número é par
        print(numero)

#

# Faça um programa que, Mostre A soma entre todos os numeros Imaperes que sao multiplos de 3 e que se encontram no intervalor de 1 a 500.

soma = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print(soma)

#

                                    # Inicializa a variável para armazenar a soma
soma = 0

                                    # Itera pelos números no intervalo de 1 a 500
for numero in range(1, 501):
                                    # Verifica se o número é ímpar e múltiplo de 3
    if numero % 2 != 0 and numero % 3 == 0:
                                    # Adiciona o número à soma total
        soma += numero

                                    # Imprime o resultado da soma
print("A soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500 é:", soma)

#

# Refaça o exercicio 09, Mostrando a tabueada de um numero que o usuario escolher, só que agora utilizando laço For.

numero = int ( input ( " Digite um número: " ) )

for i in range ( 1, 11 ):
    print(f"{numero} x {i} = {numero * i}")
    i += 1
    if i == 11:
        break
    else:
        continue
else:
    print("Fim da tabuada.")

#

                                                                # Solicita ao usuário para digitar um número para a tabuada
numero = int (input ( " Digite um número para ver sua tabuada: " ) )

                                                                # Laço for para iterar de 1 a 10 e mostrar a tabuada
print (f"Tabuada de {numero}:")

for i in range ( 1, 11 ) :
    resultado = numero * i
    print ( f"{numero} x {i} = {resultado}" )

#

# Desenvolva um programa que, Leia seia numeros inteiros e mostre a soma aoenas daqueles que forem pares. se o valor digitado for impar DESCONSIDERE-O com uma menssagem Ignorante.
                                        # Inicializa a variável para armazenar a soma
soma = 0
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        soma += numero
    else: 
        print("Número ignorado.")
print("A soma dos números pares é:", soma)

#

                                                                # Função para verificar se um número é par
def eh_par(numero):
    return numero % 2 == 0

                                                                # Inicialização da variável para armazenar a soma dos números pares
soma_pares = 0

                                                                # Loop para ler os números digitados pelo usuário
while True:
    try:
        numero = int(input("Digite um número inteiro (ou '0' para sair): "))
        if numero == 0:
            break                                               # Sai do loop se o usuário digitar 0
        if not eh_par(numero):
            print("Número ímpar ignorado.")
            continue                                            # Ignora números ímpares
        soma_pares += numero                                    # Adiciona o número par à soma
    except ValueError:
        print("Digite um número inteiro válido!")

                                                                # Exibe a soma dos números pares digitados
print(f"A soma dos números pares digitados é: {soma_pares}")

#

# Desenvolva um programa que, Leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa Progressão.

                                        # Leitura do primeiro termo e da razão da PA

primeiro_termo = int(input("Digite o primeiro termo da PA: ")) 
razao = int(input("Digite a razão da PA: "))

                                        # Loop para mostrar os 10 primeiros termos da PA

for i in range(10):
    print(primeiro_termo + i * razao)
    i += 1
    
    if i == 10:
        break
    else:
        continue
else:
    print("Fim da PA.")

#
    
                                                            # Função para calcular os termos da PA
    
def calcular_PA(primeiro_termo, razao, quantidade):
    termos = []
    for i in range(quantidade):
        termo = primeiro_termo + (i * razao)
        termos.append(termo)
    return termos

                                                            # Entrada do usuário

primeiro_termo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))

                                                            # Calculando os 10 primeiros termos

termos_PA = calcular_PA(primeiro_termo, razao, 10)

                                                            # Mostrando os termos

print("\nOs 10 primeiros termos da Progressão Aritmética são:")
for termo in termos_PA:
    print(termo, end=' ')

#
    
# Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero Primo.
    
    numero = int(input("Digite um número inteiro: "))
    
    if numero <= 1:
        print("O número não é primo.")
    else: 
        for i in range(2, numero):
            if numero % i == 0:
                print("O número não é primo.")
                break
        else:
            print("O número é primo.")

#

def verificar_primo(numero):
                                                    # Números menores que 2 não são primos
    
    if numero < 2:
        return False
    
                                                    # Verificar se o número é divisível por algum outro número além de 1 e ele mesmo
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

                                                    # Solicitar ao usuário para digitar um número inteiro

numero = int(input("Digite um número inteiro: "))

                                                    # Verificar se o número é primo ou não

if verificar_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")


#
    
# Crie um programa que, leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").lower()
frase_sem_espaco = frase.replace(" ", "")

if frase_sem_espaco == frase_sem_espaco[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")

#
    
def eh_palindromo(frase):
                                                        # Remover espaços da frase e converter para minúsculas
    
    frase_sem_espacos = frase.replace(" ", "").lower()
    
                                                        # Verificar se a frase sem espaços é igual à sua reversão
    
    if frase_sem_espacos == frase_sem_espacos[::-1]:
        return True
    else:
        return False

frase_input = input("Digite uma frase para verificar se é um palíndromo: ")

if eh_palindromo(frase_input):
    print(f'A frase "{frase_input}" é um palíndromo.')
else:
    print(f'A frase "{frase_input}" não é um palíndromo.')

#
    
# Crei um programa que leia o ano de nascimento de 10 pessoas. No final, mostre quantas pessoas ainda nao atingiram a maior idade e quantas ja são maiores.

                                            # Inicializa as variáveis para contar as pessoas maiores e menores de idade

maiores_de_idade = 0
menores_de_idade = 0

                                            # Loop para ler o ano de nascimento de 10 pessoas
for i in range(10):
    ano_nascimento = int(input("Digite o ano de nascimento da pessoa {}: ".format(i + 1)))
    
                                            # Calcula a idade da pessoa

    idade = 2023 - ano_nascimento
    if idade >= 18:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1
        print("A pessoa {} ainda não atingiu a maior idade.".format(i + 1))
        continue

                                            # Exibe o resultado

print("Há {} pessoas maiores de idade e {} pessoas menores de idade.".format(maiores_de_idade, menores_de_idade))

#

from datetime import date

                                            # Obtendo o ano atual

ano_atual = date.today().year

                                            # Contadores para armazenar a quantidade de pessoas menores e maiores de idade

menores_idade = 0
maiores_idade = 0

                                            # Loop para ler o ano de nascimento de 10 pessoas

for i in range(1, 11):
    ano_nascimento = int(input(f'Digite o ano de nascimento da pessoa {i}: '))
    idade = ano_atual - ano_nascimento

    if idade < 18:
        menores_idade += 1
    else:
        maiores_idade += 1

                                            # Exibindo o resultado
        
print(f'\nPessoas menores de idade: {menores_idade}')
print(f'Pessoas maiores de idade: {maiores_idade}')

#

# Faça um programa que leia o peso e altura de 5 pessoas e no final mostre qual foi o maior peso, a maior altura e o maior IMC.

                                            # Inicializa as variáveis para armazenar o maior peso, a maior altura e o maior IMC

maior_peso = 0
maior_altura = 0
maior_imc = 0

                                                    # Loop para ler o peso e altura de 5 pessoas

for i in range(5):
    peso = float(input("Digite o peso da pessoa {}: ".format(i + 1)))
    altura = float(input("Digite a altura da pessoa {}: ".format(i + 1)))
    
                                                    # Calcula o IMC da pessoa

#

                                                    # Inicializando variáveis para armazenar os maiores valores encontrados
maior_peso = 0
maior_altura = 0
maior_imc = 0

                                                    # Laço para ler os dados das 5 pessoas
for i in range(5):
    print(f'Pessoa {i+1}:')
    peso = float(input('Digite o peso (em kg): '))
    altura = float(input('Digite a altura (em metros): '))

                                                    # Calculando o IMC
    imc = peso / (altura ** 2)

                                                    # Verificando se os valores são os maiores encontrados até agora
    if peso > maior_peso:
        maior_peso = peso
    if altura > maior_altura:
        maior_altura = altura
    if imc > maior_imc:
        maior_imc = imc

                                                    # Mostrando os maiores valores encontrados
print(f'\nMaior peso: {maior_peso} kg')
print(f'Maior altura: {maior_altura} m')
print(f'Maior IMC: {maior_imc:.2f}')

#

# Desenvolva um programa que Leia: [1] Nome [2] Idade [3] sexo, de 5 pessoas, e no final mostre: [a] a media de idade de grupo [b] qual é o nome do homem mais velho [c] quantas mulheres tem no grupo com menos de 20 anos.

                                                    # Inicializando as variáveis para armazenar os dados

nomes = []
idades = []
sexos = []

                                                    # Loop para coletar os dados das 5 pessoas

for i in range(5):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = input(f'Digite o sexo de {nome} (M/F): ').upper()

                                                    # Adicionando os dados às listas
    
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

                                                    # Calculando a média de idade do grupo
    
media_idade = sum(idades) / len(idades)

                                                    # Encontrando o homem mais velho

homem_mais_velho = ""
idade_mais_velha = 0
for i in range(len(nomes)):
    if sexos[i] == 'M' and idades[i] > idade_mais_velha:
        homem_mais_velho = nomes[i]
        idade_mais_velha = idades[i]

                                                    # Contando mulheres com menos de 20 anos
        
mulheres_menos_vinte = sum(1 for i in range(len(nomes)) if sexos[i] == 'F' and idades[i] < 20)

                                                    # Mostrando os resultados

print(f'A média de idade do grupo é {media_idade:.1f} anos.')
print(f'O homem mais velho é {homem_mais_velho} com {idade_mais_velha} anos.')
print(f'Existem {mulheres_menos_vinte} mulheres com menos de 20 anos no grupo.')

###
