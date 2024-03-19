# Escrava um programa para aprovar um emprestimo bancario para a acompra de uma casa. o programa par vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Caucule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

# Importando a biblioteca necessária para cálculos matemáticos
import math

def calcular_prestacao_mensal(valor_casa, salario_comprador, prazo_emprestimo):
    # Convertendo o prazo do empréstimo de anos para meses
    prazo_meses = prazo_emprestimo * 12

    # Solicitando a taxa de juros anual ao usuário
    taxa_juros_anual = float(input("Digite a taxa de juros anual (%): "))
    
    # Calculando a taxa de juros mensal com base na taxa anual
    taxa_juros_mensal = (1 + (taxa_juros_anual / 100))**(1 / 12) - 1
    
    # Calculando a prestação mensal usando a fórmula de amortização
    prestacao_mensal = (valor_casa * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal)**-prazo_meses)
    
    return prestacao_mensal

# Solicitando informações ao usuário
valor_casa = float(input("Digite o valor da casa (em reais): "))
salario_comprador = float(input("Digite o salário mensal do comprador (em reais): "))
prazo_emprestimo = int(input("Digite o prazo de pagamento do empréstimo (em anos): "))

# Calculando a prestação mensal
prestacao_calculada = calcular_prestacao_mensal(valor_casa, salario_comprador, prazo_emprestimo)

# Verificando a condição de aprovação do empréstimo
if prestacao_calculada <= 0.3 * salario_comprador:
    print("Empréstimo Aprovado! Prestação Mensal: R$", round(prestacao_calculada, 2))
else:
    print("Empréstimo Negado! A prestação excede 30% do salário.")

#

# Escrava um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão: 1= para binario 2= Para octal 3= para hexadecimal

def decimal_para_binario(numero):
    return bin(numero)[2:]

def decimal_para_octal(numero):
    return oct(numero)[2:]

def decimal_para_hexadecimal(numero):
    return hex(numero)[2:].upper()

def main():
    numero = int(input("Digite um número inteiro: "))
    escolha = int(input("Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n"))

    if escolha == 1:
        resultado = decimal_para_binario(numero)
        base = 'binário'
    elif escolha == 2:
        resultado = decimal_para_octal(numero)
        base = 'octal'
    elif escolha == 3:
        resultado = decimal_para_hexadecimal(numero)
        base = 'hexadecimal'
    else:
        print("Escolha inválida.")
        return

    print(f"O número {numero} convertido para {base} é: {resultado}")

if __name__ == "__main__":
    main()

#

# Escrava um programa que leia 2 numeros inteiros e compare-os, mostrando na tela uma mensagem: 1 = O primeiro valor é maior. 2 = o segundo valor é maior. 3 = Não existe valor maior, os dois são iguais.

# Função para comparar os números e exibir a mensagem
def comparar_numeros(num1, num2):
    if num1 > num2:
        print("1 = O primeiro valor é maior.")
    elif num2 > num1:
        print("2 = O segundo valor é maior.")
    else:
        print("3 = Não existe valor maior, os dois são iguais.")

# Solicita a entrada do usuário para os dois números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Chama a função para comparar os números
comparar_numeros(num1, num2)

#

# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 1 = se ele ainda vai se alistar no exercito militar. 2 = se é a hora de se alistar. 3 = se ja do tempo do alistamento. O programa tbm deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento do jovem: "))
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f"O jovem tem {idade} anos e ainda vai se alistar no Exército.")
    print(f"Faltam {18 - idade} anos para o alistamento obrigatório.")
elif idade == 18:
    print("É hora de se alistar no Exército!")
else:
    print(f"O jovem tem {idade} anos e já passou da idade do alistamento obrigatório.")
    print(f"Já se passaram {idade - 18} anos do prazo de alistamento.")

#

# Faça um programa que leia as notas de um aluno, e caucule a media de notas mostrando uma menssagem no final de acordo com a sua media alcançada. 1 =  media abaixo de 5.0:REPROVADO. 2 = media entre 5.1 e 7.0:RECUPERAÇÃO. 3 = media de 7.1 ou superior:APROVADO. E coloque uma menssagem de motivação de acordo com cada nivel de media 1, 2, 3.

def calcular_media(notas):
    total_notas = len(notas)
    soma = sum(notas)
    media = soma / total_notas
    return media

def verificar_status_aluno(media):
    if media < 5.0:
        status = "REPROVADO"
        mensagem = "Você pode fazer melhor na próxima vez. Não desista!"
    elif media >= 5.1 and media <= 7.0:
        status = "RECUPERAÇÃO"
        mensagem = "Foco e dedicação nos estudos podem te levar à aprovação."
    else:
        status = "APROVADO"
        mensagem = "Parabéns! Seu esforço valeu a pena."
    
    return status, mensagem

def main():
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'fim' para terminar): ")
        if nota.lower() == 'fim':
            break
        notas.append(float(nota))
    
    media = calcular_media(notas)
    status, mensagem = verificar_status_aluno(media)
    
    print(f"A média do aluno é: {media:.2f}")
    print(f"Status: {status}")
    print(f"Mensagem: {mensagem}")

if __name__ == "__main__":
    main()

#
    
# Faça um program aque leia: A confederação nacional de natação precisa de um aplicativo que interprete o ano de nascimento de um atleta e mostre a sua categoria de acordo com a sua idade: 1 = ate 9 anos:Mirim. 2 = ate 14 anos:Juvenil. 3 = ate 19 anos:Junior. 4 = ate 20 anos.Senior. 5 = acima de 21 anos:Master.

# Função para determinar a categoria com base no ano de nascimento
def determinar_categoria(ano_nascimento):
    idade = 2024 - ano_nascimento

    if idade <= 9:
        return "Mirim"
    elif idade <= 14:
        return "Juvenil"
    elif idade <= 19:
        return "Junior"
    elif idade <= 20:
        return "Senior"
    else:
        return "Master"

# Solicitar ao usuário o ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

# Chamar a função para determinar a categoria e mostrar o resultado
categoria = determinar_categoria(ano_nascimento)
print(f"A categoria do atleta é: {categoria}")

#

# Crie um progra que faça a soma de 3 valores que o usuario ia digitar e mostre na tela se é possivel formar um triangulo, se sim, que ele mostre qual é o tipo de triangulo que vai se formar: 1 = EQUILATERO:todos os lados iguais. 2 = ISOSCELES:dois lados iguais. 3 = ESCALENO:todos os lados diferentes. 4 = NÃO FORMA TRIANGULO NENHUM.

def tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "EQUILATERO: todos os lados iguais."
        elif a == b or a == c or b == c:
            return "ISOSCELES: dois lados iguais."
        else:
            return "ESCALENO: todos os lados diferentes."
    else:
        return "NÃO FORMA TRIANGULO NENHUM."

def main():
    try:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))
        c = float(input("Digite o terceiro valor: "))

        resultado = tipo_triangulo(a, b, c)
        print(resultado)
    except ValueError:
        print("Por favor, digite apenas números.")

if __name__ == "__main__":
    main()

#

# Desemvolva uma logica que leia o peso e a altura de uma pessoa, caucule o seu IMC e mostre o seu status, de acordo com a tabela: 1= ABAIXO DE 1.85:abaixo do peso. 2 = ENTRE 18.5 E 25:peso ideal. 3 = 26 a 30:sobrepeso. 4 = 31 a 40:obesidade. 5 = ACIMA DE 41:obesidade morbida.
    
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def verificar_status(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "No Peso ideal"
    elif 25 <= imc < 30:
        return "Com Sobrepeso"
    elif 30 <= imc < 40:
        return "Com Obesidade"
    else:
        return "Com Obesidade mórbida"

def main():
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))

    imc = calcular_imc(peso, altura)
    status = verificar_status(imc)

    print(f"Seu IMC é {imc:.2f}, o que significa que você está {status}.")

if __name__ == "__main__":
    main()

#

# Faça um aplicativo que, Caucule de maneira Complexa, o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento. 1 = A VISTA:dinheiro_cheque_pix:10% de desconto. 2 = AVISTA NO CARTAO:5% de desconto. 3 = EM ATÉ 2X:no cartao de credito>preço normal. 3 = 3X OU MAIS:no cartao de credito>13% de juros.

def calcular_valor_produto(preco_normal, condicao_pagamento):
    if condicao_pagamento == 1:  # A VISTA: 10% de desconto
        valor_a_pagar = preco_normal * 0.9
    elif condicao_pagamento == 2:  # A VISTA NO CARTAO: 5% de desconto
        valor_a_pagar = preco_normal * 0.95
    elif condicao_pagamento == 3:  # EM ATÉ 2X: preço normal
        valor_a_pagar = preco_normal
    elif condicao_pagamento == 4:  # 3X OU MAIS: 13% de juros
        valor_a_pagar = preco_normal * 1.13
    else:
        print("Condição de pagamento inválida.")
        return None
    
    return valor_a_pagar

# Exemplo de uso
preco = float(input("Digite o preço do produto: "))
condicao = int(input("Digite a condição de pagamento (1, 2, 3 ou 4): "))

valor_final = calcular_valor_produto(preco, condicao)

if valor_final is not None:
    print(f"Valor a ser pago: R$ {valor_final:.2f}")

#

# Crie um programa que faça o computador jogar com o usuario: o jogo escolhido é JOKENPO. 

import random

def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes)

    print("Bem-vindo ao jogo Jokenpo!")
    print("Escolha sua jogada:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    escolha_usuario = int(input("Digite o número correspondente à sua escolha: "))
    escolha_usuario -= 1  # Ajuste para acessar o índice correto na lista

    if escolha_usuario < 0 or escolha_usuario >= len(opcoes):
        print("Opção inválida. Por favor, escolha novamente.")
        jogar_jokenpo()

    print(f"Você escolheu: {opcoes[escolha_usuario]}")
    print(f"O computador escolheu: {computador}")

    if opcoes[escolha_usuario] == computador:
        print("Empate!")
    elif (opcoes[escolha_usuario] == 'pedra' and computador == 'tesoura') or \
         (opcoes[escolha_usuario] == 'papel' and computador == 'pedra') or \
         (opcoes[escolha_usuario] == 'tesoura' and computador == 'papel'):
        print("Você venceu!")
    else:
        print("Você perdeu!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        jogar_jokenpo()
    else:
        print("Obrigado por jogar Jokenpo!")

jogar_jokenpo()

#

