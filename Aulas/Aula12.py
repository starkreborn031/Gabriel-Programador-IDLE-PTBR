# Criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 16:
    print("Você é menor de idade, mas já pode votar.")
else:
    print("Você é menor de idade.")

# Criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
 
nome = str(input('Qual é o seu nome?'))
if nome == 'Gabriel':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#
 
nome = str(input('Qual é o seu nome?'))
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome == 'Thiago' or nome == 'João':
    print('Que nome popular!')
elif nome == 'Maria' or nome == 'Ana':
    print('Que nome feminino!')
elif nome == 'Pedro' or nome == 'Carlos':
    print('Que nome masculino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#

