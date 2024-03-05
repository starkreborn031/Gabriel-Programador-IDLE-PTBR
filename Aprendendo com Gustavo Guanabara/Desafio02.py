# Solicitação de entrada do usuário
palavra = input("Digite uma palavra: ")
numero = input("Digite um número: ")
caractere = input("Digite um caractere especial: ")

# Verificando se a palavra é verdadeira ou falsa
e_verdadeira = palavra.isalpha()

# Verificando o tipo de escrita da palavra
tipo_escrita = "Minúscula" if palavra.islower() else "Maiúscula" if palavra.isupper() else "Mista"

# Verificando se o número é realmente um número
e_numero = numero.isdigit()

# Verificando se o caractere é um caractere especial
e_caractere_especial = len(caractere) == 1 and not caractere.isalnum()

# Exibindo informações sobre as entradas
print("\n=== Informações sobre as entradas ===")
print(f"Palavra: {palavra} - Verdadeira: {e_verdadeira} - Tipo de Escrita: {tipo_escrita}")
print(f"Número: {numero} - É Número: {e_numero} - Tipo: {type(numero)}")
print(f"Caractere: {caractere} - É Caractere Especial: {e_caractere_especial} - Tipo: {type(caractere)}")
