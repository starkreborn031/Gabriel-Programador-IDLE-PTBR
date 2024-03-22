# Solicita a entrada do usuário para os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Exibe o resultado
print(f"A soma de {numero1} e {numero2} é: {soma}")

# Solicita a entrada do usuário para os dois números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Exibe o resultado
print(f"A soma de {numero1} e {numero2} é: {soma}")

# ______________________________________________________________________________________________________________________________________

# Solicita a entrada do usuário para os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Exibe o resultado
print(f"A soma de {numero1} e {numero2} é: {soma}")

# ______________________________________________________________________________________________________________________________________

# Solicita a entrada do usuário para os dois números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Exibe o resultado
print(f"A soma de {numero1} e {numero2} é: {soma}")

# _______________________________________________________________________________________________________________________________________

# Solicitação de entrada do usuário
palavra = input("Digite uma palavra: ")
numero = input("Digite um número: ")
caractere = input("Digite um caractere especial: ")

# Verificando o tipo primitivo de cada entrada
tipo_palavra = type(palavra)
tipo_numero = type(numero)
tipo_caractere = type(caractere)

# Exibindo informações sobre as entradas
print("\n=== Informações sobre as entradas ===")
print(f"Palavra: {palavra} - Tipo: {tipo_palavra}")
print(f"Número: {numero} - Tipo: {tipo_numero}")
print(f"Caractere: {caractere} - Tipo: {tipo_caractere}")

# _______________________________________________________________________________________________________________________________________

# Solicitação de entrada do usuário
palavra = input("Digite uma palavra: ")
numero = input("Digite um número: ")
caractere = input("Digite um caractere especial: ")

# Verificando se a palavra é verdadeira ou falsa
e_verdadeira = palavra.isalpha()

# Verificando o tipo de escrita da palavra
if palavra.islower():
    tipo_escrita = "Minúscula"
elif palavra.isupper():
    tipo_escrita = "Maiúscula"
else:
    tipo_escrita = "Mista"

# Verificando o tipo primitivo de cada entrada
tipo_numero = type(numero)
tipo_caractere = type(caractere)

# Exibindo informações sobre as entradas
print("\n=== Informações sobre as entradas ===")
print(f"Palavra: {palavra} - Verdadeira: {e_verdadeira} - Tipo de Escrita: {tipo_escrita}")
print(f"Número: {numero} - Tipo: {tipo_numero}")
print(f"Caractere: {caractere} - Tipo: {tipo_caractere}")

# _______________________________________________________________________________________________________________________________________
