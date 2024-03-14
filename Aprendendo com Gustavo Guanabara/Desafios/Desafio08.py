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
