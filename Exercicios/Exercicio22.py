nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Sem considerar espaços, seu nome tem {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))

# ____________________________________________________________________________________________________________________________________________________________
