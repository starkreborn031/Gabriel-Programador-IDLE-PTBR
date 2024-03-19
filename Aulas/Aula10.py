#            Condições / Estrutura Condicional Sequencial / if : else / Conjunto de passos com ALGORITIMO

#                 Progama trabalhando 'POSSIBILIDADES DIFERENTES PARA CADA EXECUÇÃO DE TAREFA' 

#                     Tratamento diferente para decisões diferentes, Opiniões diferentes

# ______________________________________________________________________________________________________________________________________

nome = str(input('Qual é o Seu nome completo? '))
if nome == 'Gabriel de Sousa Rocha' :
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é bonito também!')
print('Seja bem vindo {} ao curso de Python!'.format(nome))

# ______________________________________________________________________________________________________________________________________

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
media = float((numero1 + numero2) / 2)

if media >= 7.0:
    print('Pabraéns, Aprovado!')

else: 
    print('Infelizmente voce esta de recuperação!')


