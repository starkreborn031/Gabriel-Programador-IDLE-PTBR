# Faça um programa que leia as notas de um aluno, e caucule a media de notas mostrando uma menssagem no final de acordo com a sua media alcançada. 1 =  media abaixo de 5.0:REPROVADO. 2 = media entre 5.1 e 7.0:RECUPERAÇÃO. 3 = media de 7.1 ou superior:APROVADO. E coloque uma menssagem de motivação de acordo com cada nivel de media 1, 2, 3.

nota_1 = float  (input('Digite sua nota de Portugues: '))
nota_2 = float  (input('Digite sua nota de Matematica: '))
nota_3 = float  (input('Digite sua nota de Ciencias: '))
nota_4 = float  (input('Digite sua nota de Historia: '))
nota_5 = float  (input('Digite sua nota de Geografia: '))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

print ('Tirando {:.1f} e {:.1f} a média do aluno é {:1f}! '.format(nota_1, nota_2, media))

#

nota_1 = float  (input('Digite sua nota de Portugues: '))
nota_2 = float  (input('Digite sua nota de Matematica: '))
nota_3 = float  (input('Digite sua nota de Ciencias: '))
nota_4 = float  (input('Digite sua nota de Historia: '))
nota_5 = float  (input('Digite sua nota de Geografia: '))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

print ('Tirando {:.1f} e {:.1f} a média do aluno é {:1f}! '.format(nota_1, nota_2, media))

if media >= 5 and media < 7:
    print ('O Aluno esta de RECUPERAÇÃO!')

#

nota_1 = float  (input('Digite sua nota de Portugues: '))
nota_2 = float  (input('Digite sua nota de Matematica: '))
nota_3 = float  (input('Digite sua nota de Ciencias: '))
nota_4 = float  (input('Digite sua nota de Historia: '))
nota_5 = float  (input('Digite sua nota de Geografia: '))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

print ('Tirando {:.1f} e {:.1f} a média do aluno é {:1f}! '.format(nota_1, nota_2, media))

if 7 > media >= 5:
    print ('O Aluno esta de RECUPERAÇÃO!')
elif media < 5:
    print ('O Aluno esta REPROVADO!')
else:
    print ('O Aluno esta APROVADO!')

#

nota_1 = float  (input('Digite sua nota de Portugues: '))
nota_2 = float  (input('Digite sua nota de Matematica: '))
nota_3 = float  (input('Digite sua nota de Ciencias: '))
nota_4 = float  (input('Digite sua nota de Historia: '))
nota_5 = float  (input('Digite sua nota de Geografia: '))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

print ('Tirando {:.1f} e {:.1f} a média do aluno é {:1f}! '.format(nota_1, nota_2, media))

if 7 > media >= 5:
    print ('O Aluno esta de RECUPERAÇÃO!')
elif media < 5:
    print ('O Aluno esta REPROVADO!')
elif media >= 7:
    print ('O Aluno esta APROVADO!')
