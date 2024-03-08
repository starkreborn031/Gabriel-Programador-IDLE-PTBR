# Cadeia de Caracteres / Manipulando Caxias de Texto em Python

frase = 'Manipulando Caxias de Texto em Python'
print(frase)  # Imprime a frase

frase = frase.upper()                    # Converte a frase em letras maiúsculas
frase = frase.lower()                    # Converte a frase em letras minúsculas
frase = frase.capitalize()               # Converte a primeira letra da frase em maiúscula
frase = frase.swapcase()                 # Troca as letras maiúsculas por minúsculas e vice-versa
frase = frase.replace('Python', 'Java')  # Substitui a palavra "Python" pela palavra "Java" na frase
frase = frase.count('Python')            # Conta o número de 'Python' aparece na frase
frase = frase.startswith('Manipulando')  # Verifica se a frase começa com a palavra "Manipulando"
frase = frase.endswith('Python')         # Verifica se a frase termina com a palavra "Python"

print(frase.split('\n')[0])  # Imprime a primeira linha da frase
print(frase.split('\n')[1])  # Imprime a segunda linha da frase
print(frase.split('\n')[2])  # Imprime a terceira linha da frase

print(frase.find('Manipulando'))  # Imprime a posição da primeira ocorrência da palavra "Manipulando" na frase
print(frase.rfind('Manipulando'))  # Imprime a posição da última ocorrência da palavra "Manipulando" na frase
print(frase.count('Manipulando'))  # Imprime o número de ocorrências da palavra "Manipulando" na frase

print(frase.find('Python'))  # Imprime a posição da primeira ocorrência da palavra "Python" na frase
print(frase.rfind('Python'))  # Imprime a posição da última ocorrência da palavra "Python" na frase
print(frase.count('Python'))  # Imprime o número de ocorrências da palavra "Python" na frase

print(frase.find('Java'))  # Imprime a posição da primeira ocorrência da palavra "Java" na frase
print(frase.rfind('Java'))  # Imprime a posição da última ocorrência da palavra "Java" na frase
print(frase.count('Java'))  # Imprime o número de ocorrência da palavra "Java" na frase

print(frase.find('Python'))                  # Procura a palavra "Python" na frase e retorna o índice do primeiro caractere da palavra
print(frase.rfind('Python'))                 # Procura a palavra "Python" na frase e retorna o índice do último caractere da palavra
print('Python' in frase)                     # Verifica se a palavra "Python" está na frase
print('Java' in frase)                       # Verifica se a palavra "Java" está na frase
print(frase.index('Python'))                 # Procura a palavra "Python" na frase e retorna
print(frase.replace('Python', 'Java'))       # Imprime a frase com a palavra "Python" substituída pela palavra "Java"
print(frase.count('Python'))                 # Imprime o número de vezes que a palavra "Python" aparece na frase
print(frase.startswith('Manipulando'))       # Verifica se a frase começa com a palavra "Manipulando"
print(frase.endswith('Python'))              # Verifica se a frase termina com a palavra "Python"
print(frase.replace('Python', 'Java', 1))    # Substitui a primeira ocorrência da palavra "Python" pela palavra "Java" na frase
print(frase.replace('Python', 'Java', 2))    # Substitui as duas primeiras ocorrências da palavra

print(len(frase))                   # Imprime o número de caracteres da frase
print(len(frase.split()))           # Imprime o número de palavras da frase
print(len(frase.split(' ')))        # Imprime o número de palavras da frase, separadas por um espaço em branco
print(len(frase.split('\n')))       # Imprime o número de linhas da frase
print(len(frase.split('\n')[6]))    # Imprime o número de tabulações da sétima linha da frase
print(len(frase.split('\n')[7]))    # Imprime o número de tabulações da oitava linha da frase
print(len(frase.split('\n')[8]))    # Imprime o número de tabulações da nona linha da frase
print(len(frase.split('\n')[9]))    # Imprime o número de tabulações da décima linha da frase
print(len(frase.split('\n')[10]))   # Imprime o número de tabulações da décima primeira linha da frase
print(len(frase.split('\t')))       # Imprime o número de tabulações da frase
print(len(frase.split('\t')[0]))    # Imprime o número de tabulações da primeira linha da frase
print(len(frase.split('\t')[1]))    # Imprime o número de tabulações da segunda linha da frase
print(len(frase.split('\t')[2]))    # Imprime o número de tabulações da terceira linha da frase
print(len(frase.split('\t')[3]))    # Imprime o número de tabulações da quarta linha da frase
print(len(frase.split('\t')[4]))    # Imprime o número de tabulações da quinta linha da frase
print(len(frase.split('\t')[5]))    # Imprime o número de tabulações da sexta linha da frase

print(frase[0:10])      # Imprime os primeiros 10 caracteres da frase
print(frase[10:])       # Imprime os caracteres a partir do 11º caractere
print(frase[0::2])      # Imprime os caracteres de 2
print(frase[10])        # Imprime o 11º caractere da frase
print(frase[-11])       # Imprime o 11º caractere a partir do final da frase
print(frase[10:15])     # Imprime os caracteres
print(frase[0])         # Imprime o primeiro caractere da frase
print(frase[-1])        # Imprime o último caractere da frase
print(frase[0:5])       # Imprime os primeiros 5 caracteres da frase
print(frase[5:])        # Imprime os caracteres a partir do 6º caractere
print(frase[0::2])      # Imprime os caracteres de 2 em 2
print(frase[1::3])      # Imprime os caracteres de 3 em 3
print(frase[::-1])      # Imprime a frase ao contrário

print(frase.strip())       # Remove os espaços em branco do início e do fim da frase
print(frase.lstrip())      # Remove os espaços em branco do início da frases
print(frase.rstrip())      # Remove os espaços em branco do fim da frase
print(frase.split())       # Divide a frase em palavras e armazena em uma lista

print(frase.upper())        # Imprime a frase em letras maiúsculas
print(frase.lower())        # Imprime a frase em letras minúsculas
print(frase.capitalize())   # Imprime a frase com a primeira letra de cada
print(frase.swapcase())     # Imprime a frase com as letras maiúsculas em minúsculas e vice-versa
print(frase.upper())        # Converte a frase em letras maiúsculas
print(frase.lower())        # Converte a frase em letras minúsculas
print(frase.capitalize())   # Converte a primeira letra da frase em maiúscula

print(frase.isalnum())              # Verifica se todos os caracteres da frase são alfanuméricos
print(frase.isalpha())              # Verifica se todos os caracteres da frase são alfabéticos
print(frase .isdigit())             # Verifica se todos os caracteres da frase são dígitos
print(frase.islower())              # Verifica se todos os caracteres da frase são minúsculos
print(frase.isupper())              # Verifica se todos os caracteres da frase são maiúsculos
print(frase.isnumeric())            # Verifica se todos os caracteres da frase são números
print(frase.isdecimal())            # Verifica se todos os caracteres da frase são dígitos decimais
print(frase.isidentifier())         # Verifica se a frase é um identificador válido
print(frase.istitle())              # Verifica se a frase está em formato de título
print(frase.isprintable())          # Verifica se a frase é imprimível
print(frase.isblank())              # Verifica se a frase está em branco
print(frase.isspace())              # Verifica se a frase é composta apenas por espaços em branco

print(frase.join('-'))       # Junta as palavras da lista em uma string, separadas pelo caractere "-"
print(frase.join(' '))       # Junta as palavras da lista em uma string, separadas por um espaço em branco
print(frase.join('\n'))      # Junta as palavras da lista em uma string, separadas por uma quebra de linha

print(frase.replace('\n', ''))      # Remove todas as quebras de linha da frase
print(frase.replace('\t', ''))      # Remove todas as tabulações da frase
print(frase.replace('\f', ''))      # Remove todas as quebras de página
print(frase.replace('\v', ''))      # Remove todas as quebras de linha vertical da frase
print(frase.replace('\r', ''))      # Remove todas as quebras de linha reversa da frase

print(frase.replace('\n', ' '))         # Substitui todas as quebras de linha por espaços em branco
print(frase.replace('\t', ' '))         # Substitui todas as tabulações por espaços em branco
print(frase.replace('\f', ' '))         # Substitui todas as quebras de página por espaços em branco
print(frase.replace('\v', ' '))         # Substitui todas as quebras de linha vertical por espaços em branco
print(frase.replace('\r', ' '))         # Substitui todas as quebras de linha reversa por espaços em branco

print(frase.replace('\n', '\f'))    # Substitui todas as quebras de linha por quebras de página
print(frase.replace('\n', '\t'))    # Substitui todas as quebras de linha por tabulações
print(frase.replace('\t', '\n'))    # Substitui todas as tabulações por quebras de linha
print(frase.replace('\f', '\t'))    # Substitui todas as quebras de página por tabulações
print(frase.replace('\v', '\n'))    # Substitui todas as quebras de linha vertical por quebras de linha
print(frase.replace('\r', '\n'))    # Substitui todas as quebras de linha reversa por quebras de linha
print(frase.replace('\n', '\v'))    # Substitui todas as quebras de linha por quebras de linha vertical
print(frase.replace('\t', '\v'))    # Substitui todas as tabulações por quebras

print(frase.splitlines())       # Divide a frase em linhas e armazena em uma lista
print(frase.split(','))         # Divide a frase em palavras, separadas por uma vírgula
print(frase.split('.'))         # Divide a frase em palavras, separadas por um ponto
print(frase.split('!'))         # Divide a frase em palavras, separadas por uma exclamação
print(frase.split())            # Divide a frase em palavras
print(frase.split(' '))         # Divide a frase em palavras, separadas por um espaço em branco
print(frase.split('-'))         # Divide a frase em palavras, separadas pelo caractere "-"
print(frase.split(' '))         # Divide a frase em palavras, separadas por um espaço em branco
print(frase.split('\n'))        # Divide a frase em palavras, separadas por uma quebra de linha
print(frase.split('\t'))        # Divide a frase em palavras, separadas por uma tabulação
print(frase.split('\f'))        # Divide a frase em palavras, separadas por uma quebra de página
print(frase.splitlines(True))   # Divide a frase em linhas e armazena em uma lista, mantendo as quebras de linha
print(frase.splitlines(False))  # Divide a frase em linhas e armazena em uma lista, removendo as quebras de linha

print(frase.center(50, '-'))        # Centraliza a frase em 50 caracteres, usando o caractere "-" como preenchimento
print(frase.center(50))             # Centraliza a frase em 50 caracteres
print(frase.rjust(50))              # Justifica a frase à direita em 50 caracteres
print(frase.ljust(50))              # Justifica a frase à esquerda em 50 caracteres
print(frase.rjust(50, '-'))         # Justifica a frase à direita em 50 caracteres, usando o caractere "-" como preenchimento
print(frase.rjust(50, '-'))         # Justifica a frase à direita, usando o caractere "-" como preenchimento
print(frase.ljust(50, '-'))         # Justifica a frase
print(frase.rjust(50, '-'))         # Justifica a frase à esquerda, usando o caractere "-" como preenchimento
print(frase.zfill(50))              # Preenche a frase com zeros à esquerda, para que ela tenha 50 caracteres

print(frase.translate(str.maketrans('aeiou', 'AEIOU')))                             # Traduz as vogais da frase para maiúsculas
print(frase.translate(str.maketrans('AEIOU', 'aeiou')))                             # Traduz as vogais
print(frase.translate(str.maketrans('0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')))   # Traduz os números para letras maiúsculas
print(frase.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789')))   # Traduz as letras maiúsculas para números
print(frase.translate(str.maketrans('0123456789', 'abcdefghijklmnopqrstuvwxyz')))   # Traduz os números para letras minúsculas
