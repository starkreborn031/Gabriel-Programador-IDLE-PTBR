# Desenvolva um programa que, Leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa Progressão.

primeiro_0 = int ( input ( " Digite o primeiro termo: " ) )
razao_0 = int ( input ( " Digite a razão: " ) )

for count in range(1, 11, 1):
    print ( ' {} ' .format ( count ), end=' → ' )
print ( 'ACABOU ! ' )

#
    
primeiro_0 = int ( input ( " Digite o primeiro termo: " ) )
razao_0 = int ( input ( " Digite a razão: " ) )

for count in range(primeiro_0, 11, razao_0):
    print ( ' {} ' .format ( count ), end=' → ' )

#

   
primeiro_0 = int ( input ( " Digite o primeiro termo: " ) )
razao_0 = int ( input ( " Digite a razão: " ) )

decimo_termo = primeiro_0 + (10 - 1) * razao_0

for count in range ( primeiro_0, decimo_termo + razao_0, razao_0 ) :
    print ( ' {} ' .format ( count ), end=' → ' )

#
    
