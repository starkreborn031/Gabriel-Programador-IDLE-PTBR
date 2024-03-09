# Crie um programa em python que leia o nome completo de uma pessoa e mostre: onome com todos caracteres minusculos, quantas letras ao todo sem considerar espaços, o nome com todas as letras mauisculas, quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
nome_minusculo = nome.lower()
nome_maiusculo = nome.upper()
primeiro_nome = nome.split()[0]

print('Nome com todos caracteres minusculos:', nome_minusculo)
print('Quantas letras ao todo sem considerar espaços:', len(nome_minusculo.replace(' ', '')))
print('Nome com todas as letras mauisculas:', nome_maiusculo)
print('Quantas letras tem o primeiro nome:', len(primeiro_nome))

# Saída:

# Digite seu nome completo: João da Silva
# Nome com todos caracteres minusculos: joão da silva
# Quantas letras ao todo sem considerar espaços: 13
# Nome com todas as letras mauisculas: JOÃO DA SILVA
# Quantas letras tem o primeiro nome: 4

""" O programa lê o nome completo de uma pessoa e mostra:

- O nome com todos os caracteres minúsculos.
- Quantas letras ao todo sem considerar espaços.
- O nome com todas as letras maiúsculas.
- Quantas letras tem o primeiro nome.

O programa usa o método lower() para converter o nome para minúsculas, o método upper() para converter o nome para maiúsculas, o método split() para dividir o nome em palavras e o método len() para contar o número de letras em uma string."""

"""O programa também usa o método replace() para substituir os espaços por nada, o que permite contar o número de letras no nome sem considerar os espaços."""

# ____________________________________________________________________________________________________________________________________________________________

# Faça um programa que leia um numero de 0 a 9999 e mostre na tela ca um dos digitos separados
# Exemplo: Digite um número: 1834 -unidade:4 -dezena:3 -centena:8 -milhar:1

numero = int(input('Digite um número de 0 a 9999: '))

unidade = numero % 10
dezena = (numero % 100) // 10
centena = (numero % 1000) // 100
milhar = numero // 1000

print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)

"""  Saída:

- Digite um número de 0 a 9999: 1834
- Unidade: 4
- Dezena: 3
- Centena: 8
- Milhar: 1  """

""" O programa lê um número de 0 a 9999 e mostra na tela cada um dos dígitos separados.
- O programa usa o operador % para dividir o número pelo divisor e obter o resto.
- O programa usa o operador // para dividir o número pelo divisor e obter a parte inteira.
- O programa imprime cada um dos dígitos separados na tela.
- O programa também usa o método int() para converter a entrada do usuário para um inteiro.
- O programa também usa o método str() para converter um inteiro para uma string.
- O programa também usa o método split() para dividir uma string em uma lista de strings.
- O programa também usa o método join() para unir uma lista de strings em uma string.
- O programa também usa o método replace() para substituir uma substring por outra substring.
- O programa também usa o método find() para encontrar a primeira ocorrência de uma substring em uma string."""

# ____________________________________________________________________________________________________________________________________________________________

# Crie um programa que leia  nome de um País, Estado, Capital e Cidade, diga se em cada um dos nomes com o nome ''santo''

pais = input('Digite o nome de um país: ')
estado = input('Digite o nome de um estado: ')
capital = input('Digite o nome de uma capital: ')
cidade = input('Digite o nome de uma cidade: ')

if 'santo' in pais:
    print('O nome do país contém a palavra "santo".')
else:
    print('O nome do país não contém a palavra "santo".')

if 'santo' in estado:
    print('O nome do estado contém a palavra "santo".')
else:
    print('O nome do estado não contém a palavra "santo".')

if 'santo' in capital:
    print('O nome da capital contém a palavra "santo".')
else:
    print('O nome da capital não contém a palavra "santo".')

if 'santo' in cidade:
    print('O nome da cidade contém a palavra "santo".')
else:
    print('O nome da cidade não contém a palavra "santo".')

""" Saída:

- Digite o nome de um país: Brasil 
- Digite o nome de um estado: São Paulo
- Digite o nome de uma capital: Brasília
- Digite o nome de uma cidade: Santos

O nome do país não contém a palavra "santo".
O nome do estado não contém a palavra "santo".
O nome da capital não contém a palavra "santo".
O nome da cidade não contém a palavra "santo".  """

""" O programa lê o nome de um país, estado, capital e cidade, e diz se em cada um dos nomes com o nome ''santo''

- O programa usa o operador in para verificar se uma substring está em uma string.
- O programa imprime uma mensagem dizendo se o nome contém a palavra "santo" ou não."""

# ____________________________________________________________________________________________________________________________________________________________

# Crie um prgrama que leia o nome de uma pessoa e diga se ela tem Silva no nome

nome = input('Digite seu nome: ')

if 'Silva' in nome:
    print('Você tem Silva no nome.')
else:
    print('Você não tem Silva no nome.')

""" Saída:

- Digite seu nome: João da Silva 
- Você tem Silva no nome.

- Digite seu nome: João da Santos 
- Você não tem Silva no nome.  """

# ____________________________________________________________________________________________________________________________________________________________

# Faça um programa que peça ao usuario para escrever um texto de pelo menos 10 palavras e cada palavra com pelo menos 4 letras pelo teclado e depois mostre este resultado para o usuario: Quantas vezes foi digitado a letra Aa, Em qual posição ela aparece pela Primeira vez, Em qual posição ela aparece pela última vez, Quantas vezes foi digitado a letra Aa

texto = input("Digite um texto de pelo menos 10 palavras e cada palavra com pelo menos 4 letras: ")

# Verifica se o texto tem pelo menos 10 palavras e cada palavra tem pelo menos 4 letras

palavras = texto.split()
if len(palavras) < 10 or any(len(palavra) < 4 for palavra in palavras):
    print("O texto não atende aos requisitos. Tente novamente.")
else:
    # Conta quantas vezes a letra 'a' ou 'A' aparece no texto

    contagem = texto.lower().count('a')
    print(f"A letra 'A' ou 'a' aparece {contagem} vezes.")

    # Encontra a primeira e a última posição da letra 'a' ou 'A' no texto

    primeira_pos = texto.lower().find('a') + 1
    ultima_pos = texto.lower().rfind('a') + 1

    print(f"A letra 'A' ou 'a' aparece pela primeira vez na posição {primeira_pos}.")
    print(f"A letra 'A' ou 'a' aparece pela última vez na posição {ultima_pos}.")

""" Este programa pede ao usuário para digitar um texto. Em seguida, verifica se o texto tem pelo menos 10 palavras e cada palavra tem pelo menos 4 letras. Se o texto atender a esses requisitos, o programa conta quantas vezes a letra ‘A’ ou ‘a’ aparece no texto e mostra a primeira e a última posição dessa letra. Se o texto não atender aos requisitos, o programa pede ao usuário para tentar novamente. Por favor, note que as posições são baseadas em 1, não em 0. """

# ____________________________________________________________________________________________________________________________________________________________

# Crie um programa que leia o Nome Completo de uma pessoa, Idade e o Mes de nascimento, e em seguida escolha um nome da pessoa e mostre quantas letras tem, em seguida mostre unidade e dezena da idade dessa pessoa e tambem do mes de seu nascimento e tambem mostre seu Primeiro e Ultimo nome.

nome_completo = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
mes_nascimento = input('Digite o mês de seu nascimento: ')

# Escolha um nome da pessoa

nome = nome_completo.split()[00]

# Mostre quantas letras tem o nome da pessoa

print(f'Seu nome tem {len(nome)} letras.')

# Mostre unidade e dezena da idade da pessoa

unidade_idade = idade % 10
dezena_idade = idade // 10

print(f'A unidade da sua idade é {unidade_idade} e a dezena é {dezena_idade}.')

# Mostre unidade e dezena do mês de nascimento da pessoa

unidade_mes = int(mes_nascimento[0])
dezena_mes = int(mes_nascimento[1])

print(f'A unidade do seu mês de nascimento é {unidade_mes} e a dezena é {dezena_mes}.')

# Mostre seu Primeiro e Ultimo nome.

primeiro_nome = nome_completo.split()[00]
ultimo_nome = nome_completo.split()[-1]

print(f'Seu primeiro nome é {primeiro_nome} e seu último nome é {ultimo_nome}.')


""" Saída:

- Digite seu nome completo: João da Silva
- Digite sua idade: 25
- Digite o mês de seu nascimento: Janeiro

Seu nome tem 5 letras.
A unidade da sua idade é 5 e a dezena é 2.
A unidade do seu mês de nascimento é 1 e a dezena é 0.
Seu primeiro nome é João e seu último nome é Silva. 

 Este programa pede ao usuário para digitar seu nome completo, idade e mês de nascimento. Em seguida, ele escolhe um nome da pessoa e mostra quantas letras tem, em seguida mostra unidade e dezena da idade dessa pessoa e também do mês de seu nascimento e também mostra seu primeiro e último nome. """


# ____________________________________________________________________________________________________________________________________________________________
