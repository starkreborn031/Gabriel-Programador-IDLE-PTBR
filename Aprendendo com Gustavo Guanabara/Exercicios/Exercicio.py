# Solicitação de entrada do usuário
a = input('Digite o seu Nome, sua idade, sua altura e sua peso: ')
b = input('Digite qual sua cor favorita, um nome de um amigo, a idade e sua altura: ')
c = input('Digite em poucas palavras, seu proposito de vida, um valor em numero que voce quer como salario: ')
#
print("\n=== Informações sobre as entradas ===")
print('O tipo primitivo desse valor é', type(a))
print('O Texto acima é Alfabetico? {}'.format(a.isalpha()))
print('O Texto acima é Numerico? {}'.format(a.isnumeric()))
print('O Texto acima é Somavél? {}'.format(a.isalnum()))
