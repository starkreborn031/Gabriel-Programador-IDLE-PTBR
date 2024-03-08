# Cadeia de Caracteres / Manipulando Caxias de Texto em Python

nome = 'Gabriel De Sousa Rocha'
print(nome)

print(nome)                             # Imprime o nome completo
print(nome[0])                          # Imprime a primeira letra do nome
print(nome[0:5])                        # Imprime as primeiras 5 letras do nome
print(nome[-5:])                        # Imprime as últimas 5 letras do nome
print(nome[::-1])                       # Imprime o nome ao contrário
print(nome.center(50, '*'))             # Imprime o nome centralizado em 50 caracteres, com asteriscos ao redor
print(nome.ljust(50, '*'))              # Imprime o nome alinhado à esquerda em 50 caracteres, com asteriscos
print(nome.ljust(50))                   # Imprime o nome alinhado à esquerda em 50 caracteres
print(nome.rjust(50))                   # Imprime o nome alinhado à direita em 50 caracteres
print(nome.strip())                     # Imprime o nome sem os espaços em branco no início e no fim
print(nome.lstrip())                    # Imprime o nome sem os espaços em branco no início
print(nome.rstrip())                    # Imprime o nome sem os espaços em branco no fim
print(nome.replace(' ', ''))            # Imprime o nome sem os espaços em branco
print(nome.replace(' ', '-'))           # Imprime o nome com um traço entre cada palavra
print(nome.replace(' ', '_'))           # Imprime o nome com um sublinhado entre cada palavra
print(nome.count(' '))                  # Imprime o número de espaços em branco no nome
print(nome.find(' '))                   # Imprime o índice do primeiro espaço em branco no nome
print(nome.rfind(' '))                  # Imprime o índice do último espaço em branco no nome
print(nome.index('G'))                  # Imprime o índice da primeira vez que a letra 'G' aparece no nome
print(nome.rindex('G'))                 # Imprime o índice da última vez que a letra 'G' aparece no nome
print(nome.index('S'))                  # Imprime o índice da primeira vez que a letra 'S' aparece no nome
print(nome.rindex('S'))                 # Imprime o índice da última vez que a letra 'S' aparece no nome
print(nome.startswith('G'))             # Imprime True se o nome começa com a letra 'G'
print(nome.endswith('a'))               # Imprime True se o nome termina com a letra 'a'
print(nome.isupper())                   # Imprime True se o nome está em letras maiusculas
print(nome.islower())                   # Imprime True se o nome está em letras minúsculas
print(nome.istitle())                   # Imprime True se o nome está em letras maiúsculas e minúsculas, com a primeira letra de cada palavra maiúscula
print(nome.isnumeric())                 # Imprime True se o nome é numérico
print(nome.isalnum())                   # Imprime True se o nome é alfanumérico
print(nome.isalpha())                   # Imprime True se o nome é alfabético
print(nome.isdigit())                   # Imprime True se o nome é numérico
print(nome.isidentifier())              # Imprime True se o nome é um identificador válido em Python
print(nome.isprintable())               # Imprime True se o nome é imprimível
print(nome.isdecimal())                 # Imprime True se o nome é decimal
print(nome.isfloat())                   # Imprime True se o nome é um número de ponto flutuante
print(nome.iscomplex())                 # Imprime True se o nome é um número complexo
print(nome.isinteger())                 # Imprime True se o nome é um número inteiro
print(nome.ishex())                     # Imprime True se o nome é hexadecimal
print(nome.isoctal())                   # Imprime True se o nome é octal
print(nome.isbinary())                  # Imprime True se o nome é binário
print(nome.isbase64())                  # Imprime True se o nome é base64
print(nome.isbase32())                  # Imprime True se o nome é base32
print(nome.isbase16())                  # Imprime True se o nome é base16
print(nome.isbase8())                   # Imprime True se o nome é base8
print(nome.isbase4())                   # Imprime True se o nome é base4
print(nome.isbase2())                   # Imprime True se o nome é base2
print(nome.replace('a', 'o'))           # Imprime o nome com a letra 'a' trocada pela letra 'o'
print(nome.replace('a', 'o', 4))        # Imprime o nome com as primeiras 4 letras 'a' trocadas pela letra 'o'<ctrl63> 
print(nome.replace('a', 'o', 5))        # Imprime o nome com as primeiras 5 letras '
print(nome.replace('a', 'o', 3))        # Imprime o nome com as primeiras 3 letras 'a' trocadas pela letra 'o'
print(nome.replace('a', 'o', 2))        # Imprime o nome com as primeiras 2 letras 'a' trocadas pela letra 'o'
print(nome.replace('a', 'o', 1))        # Imprime o nome com a primeira letra 'a' trocada
print(nome.split('-'))                  # Imprime o nome em uma lista de palavras separadas por traço
print(nome.split('_'))                  # Imprime o nome em uma lista de palavras separadas por sublinhado
print(nome.split('.'))                  # Imprime o nome em uma lista
print(nome.split(' '))                  # Imprime o nome em uma lista de palavras separadas por espaço
print(nome.split('\n'))                 # Imprime o nome em uma lista de palavras separadas por quebra de linha
print(nome.split())                     # Imprime o nome em uma lista de palavras
print(nome.join('-'))                   # Imprime a lista de palavras em uma com um traço entre cada palavra
print(nome.join('_'))                   # Imprime a lista de palavras em uma com um sublinhado entre cada palavra
print(nome.join('.'))                   # Imprime a lista de palavras em uma com um ponto entre cada palavra
print(nome.join(', '))                  # Imprime a lista de palavras em uma com cada palavra separada por vírgula e espaço
print(nome.join(' - '))                 # Imprime a lista de palavras em uma com cada palavra separada por traço e espaço
print(nome.join(' '))                   # Imprime a lista de palavras em uma
print(nome.join(''))                    # Imprime a lista de palavras em uma sem espaços em branco
print(nome.join('\n'))                  # Imprime a lista de palavras em uma com cada palavra em uma linha diferente
print(nome.join('\t'))                  # Imprime a lista de palavras em uma com cada palavra tabulada
print(nome.join('\v'))                  # Imprime a lista de palavras em uma com cada palavra com um espaço vertical
print(nome.upper())                     # Imprime o nome em letras maiúsculas
print(nome.lower())                     # Imprime o nome em letras minúsculas
print(nome.title())                     # Imprime o nome com a primeira letra
print(nome.swapcase())                  # Imprime o nome com as letras maiúsculas e minúsculas trocadas
print(nome.capitalize())                # Imprime o nome com a primeira letra maiúscula e as demais minúsculas
print(nome.casefold())                  # Imprime o nome com todas as letras minúsculas
print(nome.encode('utf-8'))             # Imprime o nome em bytes codificados em UTF-8
print(nome.decode('utf-8'))             # Imprime o nome decodificado
print(nome.encode('latin-1'))           # Imprime o nome em bytes codificados em Latin-1
print(nome.decode('latin-1'))           # Imprime o nome decodificado
print(nome.encode('ascii'))             # Imprime o nome em bytes codificados em ASCII
print(nome.decode('ascii'))             # Imprime o nome decodificado
print(nome.encode('utf-16'))            # Imprime o nome em bytes codificados em UTF-16
print(nome.decode('utf-16'))            # Imprime o nome decodificado
print(nome.count('a'))                  # Imprime o número de vezes que a letra 'a' aparece no nom
print(nome.find('a'))                   # Imprime o índice da primeira vez que a letra 'a' aparece no nome
print(nome.rfind('a'))                  # Imprime o índice da última vez que a letra 'a'
