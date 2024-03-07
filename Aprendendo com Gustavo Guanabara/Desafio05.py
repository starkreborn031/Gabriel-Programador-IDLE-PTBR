
# Pedindo ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Calculando o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Mostrando o antecessor e o sucessor
print("O antecessor de", numero, "é", antecessor)
print("O sucessor de", numero, "é", sucessor)

#_______________________________________________________________________________________________________________________________________

# Importando a biblioteca math para calcular a raiz quadrada
import math

# Pedindo ao usuário para digitar um número
numero = float(input("Digite um número: "))

# Calculando o dobro, o triplo e a raiz quadrada
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = math.sqrt(numero)

# Mostrando os resultados
print(f"O dobro de {numero} é {dobro}.")
print(f"O triplo de {numero} é {triplo}.")
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")

#_______________________________________________________________________________________________________________________________________

# Pedindo ao usuário para digitar as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calculando a média das notas
media = (nota1 + nota2) / 2

# Mostrando a média
print(f"A média das notas é: {media}")

#_______________________________________________________________________________________________________________________________________

# Pedindo ao usuário para digitar um valor em quilômetros
quilometros = float(input("Digite o valor em quilômetros: "))

# Convertendo quilômetros em metros, centímetros e milímetros
metros = quilometros * 1000
centimetros = quilometros * 100000  # 1000 metros * 100 centímetros
milimetros = quilometros * 1000000  # 1000 metros * 1000 milímetros

# Mostrando os resultados
print(f"{quilometros} quilômetro(s) é igual a {metros} metro(s).")
print(f"{quilometros} quilômetro(s) é igual a {centimetros} centímetro(s).")
print(f"{quilometros} quilômetro(s) é igual a {milimetros} milímetro(s).")

#_______________________________________________________________________________________________________________________________________

# Pedindo ao usuário para digitar um número inteiro
numero = int(input("Digite um número para ver sua tabuada: "))

# Mostrando a tabuada do número
print(f"Tabuada de {numero}:")
for i in range(1, 11):  # Loop de 1 a 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#_______________________________________________________________________________________________________________________________________

# Pedindo ao usuário para digitar a quantidade de dinheiro em reais
dinheiro_em_reais = float(input("Digite a quantia de dinheiro em reais: "))

# Definindo a cotação do dólar
cotacao_dolar = 3.27

# Calculando a quantidade de dólares que a pessoa pode trocar
quantidade_dolares = dinheiro_em_reais / cotacao_dolar

# Mostrando o resultado
print(f"Com R${dinheiro_em_reais:.2f}, você pode trocar por aproximadamente ${quantidade_dolares:.2f}.")

#_______________________________________________________________________________________________________________________________________

# Pede ao usuário a largura e altura da parede
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área
area = largura * altura

# Calcula a quantidade de tinta necessária, considerando que 1 litro pinta 2m²
tinta_necessaria = area / 2

print(f"A área da sua parede é de {area}m².")
print(f"Você vai precisar de {tinta_necessaria} litro(s) de tinta para pintá-la.")

#_______________________________________________________________________________________________________________________________________

# Inicializando uma lista para armazenar os produtos e seus preços
produtos = []

# Pedindo ao usuário para inserir o nome e preço de 5 produtos
for i in range(5):
    nome_produto = input(f"Digite o nome do produto {i + 1}: ")
    preco_produto = float(input(f"Digite o preço do produto {i + 1} (apenas números): R$"))

    # Armazenando o nome e preço na lista de produtos
    produtos.append({"nome": nome_produto, "preco": preco_produto})

# Calculando o novo preço com 5% de desconto e mostrando os resultados
print("\nNovos preços com 5% de desconto:")
for produto in produtos:
    preco_com_desconto = produto["preco"] * 0.95  # Aplicando um desconto de 5%
    print(f"{produto['nome']}: R${preco_com_desconto:.2f}")

#_______________________________________________________________________________________________________________________________________

# Pedindo ao usuário para inserir o nome completo e o salário
nome_completo = input("Digite o nome completo do funcionário: ")
salario_bruto = float(input("Digite o salário bruto do funcionário (apenas números): R$"))

# Definindo as faixas de desconto de INSS
faixas_inss = [(0, 1045.00, 0.075), (1045.01, 2089.60, 0.09), (2089.61, 3134.40, 0.12), (3134.41, 6101.06, 0.14)]

# Calculando o desconto de INSS
desconto_inss = 0
for faixa in faixas_inss:
    if salario_bruto > faixa[0]:
        desconto_inss += min(salario_bruto - faixa[0], faixa[1] - faixa[0] + 0.01) * faixa[2]

# Definindo as faixas de desconto de Imposto de Renda
faixas_ir = [(0, 1903.98, 0, 0), (1903.99, 2826.65, 0.075, 142.80), (2826.66, 3751.05, 0.15, 354.80),
             (3751.06, 4664.68, 0.225, 636.13), (4664.69, float('inf'), 0.275, 869.36)]

# Calculando o desconto de Imposto de Renda
base_calculo_ir = salario_bruto - desconto_inss
desconto_ir = 0

for faixa in faixas_ir:
    if base_calculo_ir > faixa[0]:
        desconto_ir += (min(base_calculo_ir, faixa[1]) - faixa[0]) * faixa[2] - faixa[3]

# Calculando o salário líquido
salario_liquido = salario_bruto - desconto_inss - desconto_ir

# Mostrando os resultados
print("\nResumo dos Descontos:")
print(f"Nome do funcionário: {nome_completo}")
print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"Desconto de INSS: R${desconto_inss:.2f}")
print(f"Desconto de Imposto de Renda: R${desconto_ir:.2f}")
print(f"Salário líquido: R${salario_liquido:.2f}")

#_______________________________________________________________________________________________________________________________________

