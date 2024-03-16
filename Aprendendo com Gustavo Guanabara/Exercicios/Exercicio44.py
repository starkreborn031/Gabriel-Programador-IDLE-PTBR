# Faça um aplicativo que, Caucule de maneira Complexa, o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento.
'''
[1] = A VISTA:dinheiro_cheque_pix:10% de desconto. 
[2] = AVISTA NO CARTAO:5% de desconto. 
[3] = EM ATÉ 2X:no cartao de credito>preço normal. 
[4] = 3X OU MAIS:no cartao de credito>13% de juros.
'''
#

print (' {:=^40} ' .format (' STARK TECH MG '))

preço = float (input (' Digite o preço do Produto: R$'))

 
print('''  
        [1] = A VISTA:     Dinheiro, Cheque, PIX:     10% de desconto.
        [2] = A VISTA:     Em cartao de debito:     Até 5% de desconto. 
        [3] = EM ATÉ 2X:   Em cartao de credito:    preço normal. 
        [4] = 3X OU MAIS:  Em cartao de credito:    13% de juros. 
    ''')

opção = int ( input (' Digite a opção de pagamento: ' ) )

if opção == 1:
    total = preço - (preço * 10 / 100)

else:
    print (' Opção inválida! ')

print ( 'Sua Compra de R${:.2f} e o valor a ser pago é R${:.2f} ' .format ( preço, total ) )

#

print (' {:=^40} ' .format (' STARK TECH MG '))

preço = float (input (' Digite o preço do Produto: R$'))

print('''  
        [1] = A VISTA:     Dinheiro, Cheque, PIX:     10% de desconto.
        [2] = A VISTA:     Em cartao de debito:     Até 5% de desconto. 
        [3] = EM ATÉ 2X:   Em cartao de credito:    preço normal. 
        [4] = 3X OU MAIS:  Em cartao de credito:    13% de juros. 
    ''')

opção = int ( input (' Digite a opção de pagamento: ' ) )

if opção == 1:
    total = preço - (preço * 10 / 100)

elif opção == 2:
    total = preço - (preço * 5 / 100)

else:
    print (' Opção inválida! ')

print ( 'Sua Compra de R${:.2f} e o valor a ser pago é R${:.2f} ' .format ( preço, total ) )

#

print (' {:=^40} ' .format (' STARK TECH MG '))

preço = float (input (' Digite o preço do Produto: R$'))

print('''  
        [1] = A VISTA:     Dinheiro, Cheque, PIX:     10% de desconto.
        [2] = A VISTA:     Em cartao de debito:     Até 5% de desconto. 
        [3] = EM ATÉ 2X:   Em cartao de credito:    preço normal. 
        [4] = 3X OU MAIS:  Em cartao de credito:    13% de juros. 
    ''')

opção = int ( input (' Digite a opção de pagamento: ' ) )

if opção == 1:
    total = preço - (preço * 10 / 100)

elif opção == 2:
    total = preço - (preço * 5 / 100)

elif opção == 3:
    total = preço
    parcela = total / 2
    print ( 'Sua Compra sera parcelada em {}x de R${:.2f}'.format (2, parcela ) )

else:
    print (' Opção inválida! ')

print ( 'Sua Compra de R${:.2f} e o valor a ser pago é R${:.2f} ' .format ( preço, total ) )

#

print (' {:=^40} ' .format (' STARK TECH MG '))

preço = float (input (' Digite o preço do Produto: R$'))

print('''  
        [1] = A VISTA:     Dinheiro, Cheque, PIX:     10% de desconto.
        [2] = A VISTA:     Em cartao de debito:     Até 5% de desconto. 
        [3] = EM ATÉ 2X:   Em cartao de credito:    preço normal. 
        [4] = 3X OU MAIS:  Em cartao de credito:    13% de juros. 
    ''')

opção = int ( input (' Digite a opção de pagamento: ' ) )

if opção == 1:
    total = preço - (preço * 10 / 100)

elif opção == 2:
    total = preço - (preço * 5 / 100)

elif opção == 3:
    total = preço
    parcela = total / 2
    print ( 'Sua Compra sera parcelada em {}x de R${:.2f}'.format (2, parcela ) )

elif opção == 4:
    total = preço + (preço * 13 / 100)
    total_parcelas = int ( input ( ' Quantas pparcelas deseja? ' ) )
    parcela = total / total_parcelas
    print ( ' Sua Compra sera parcelada em {}x de R${:.2f}'.format (total_parcelas, parcela ))

else:
    print (' Opção inválida! ')

print ( 'Sua Compra de R${:.2f} e o valor a ser pago é R${:.2f} ' .format ( preço, total ) )

#
