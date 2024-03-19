#Você pode fazer isso de várias maneiras em Python, uma das mais comuns é utilizando a função trunc() do módulo math, que serve para truncar o número real, descartando sua parte fracionária. Aqui está um exemplo de como isso pode ser feito:


# Importando a função trunc do módulo math
from math import trunc

# Lendo um número real do teclado
num = float(input("Digite um número real: "))

# Mostrando a porção inteira do número
print("A porção inteira de {} é {}".format(num, trunc(num)))


# Outra maneira, sem precisar importar a função trunc do módulo math, é simplesmente converter o número real para inteiro diretamente. Isso também descartará a parte fracionária do número:____________________________________________________________________________________________________________________________________


# Lendo um número real do teclado
num = float(input("Digite um número real: "))

# Mostrando a porção inteira do número, convertendo para inteiro
print("A porção inteira de {} é {}".format(num, int(num)))

# Ambos os métodos irão ler um número real digitado pelo usuário e imprimir sua porção inteira, descartando a parte decimal.________________________________________________________________________________________________________________________________________________________________


# Para calcular o comprimento da hipotenusa de um triângulo retângulo em Python, você pode usar o Teorema de Pitágoras, que afirma que a hipotenusa ao quadrado é igual à soma dos quadrados dos catetos. Para isso, você pode utilizar a função hypot() do módulo math, que já realiza esse cálculo internamente. Aqui está um exemplo de como fazer isso:

# Importando a função hypot do módulo math
from math import hypot

# Lendo o comprimento do cateto oposto
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))

# Lendo o comprimento do cateto adjacente
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calculando a hipotenusa
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Mostrando o comprimento da hipotenusa
print("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa))

# Neste código, hypot() faz todo o cálculo necessário para encontrar a hipotenusa, simplificando o processo e evitando a necessidade de elevar os catetos ao quadrado e somá-los manualmente antes de tirar a raiz quadrada. Além disso, ele é mais preciso e eficiente para este tipo de cálculo.

#_______________________________________________________________________________________________________________________________________________________________


# Para calcular o seno, cosseno e tangente de um ângulo em Python, você pode usar o módulo math, que fornece funções como sin(), cos() e tan() para esses cálculos. É importante lembrar que essas funções esperam que o ângulo esteja em radianos, não em graus. Portanto, você precisará converter o ângulo de graus para radianos antes de usar essas funções. Aqui está como você pode fazer isso:

# Importando o módulo math
import math

# Lendo um ângulo em graus
angulo_graus = float(input("Digite o ângulo em graus: "))

# Convertendo o ângulo para radianos
angulo_radianos = math.radians(angulo_graus)

# Calculando o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Mostrando os resultados
print("Seno de {:.2f}°: {:.2f}".format(angulo_graus, seno))
print("Cosseno de {:.2f}°: {:.2f}".format(angulo_graus, cosseno))
print("Tangente de {:.2f}°: {:.2f}".format(angulo_graus, tangente))

# Este programa primeiro pede ao usuário para inserir um ângulo em graus. Em seguida, converte esse ângulo para radianos usando a função math.radians(). Depois disso, calcula o seno, cosseno e tangente desse ângulo em radianos, utilizando as funções math.sin(), math.cos() e math.tan(), respectivamente. Finalmente, o programa imprime os valores calculados de seno, cosseno e tangente na tela.

#_______________________________________________________________________________________________________________________________________________________________


# Para criar um programa que sorteie um entre quatro alunos, você pode usar a função choice() da biblioteca random do Python, que seleciona aleatoriamente um item de uma lista. Primeiro, você solicita os nomes dos alunos via teclado, armazena-os em uma lista e, em seguida, usa a função choice() para escolher um deles. Veja como isso pode ser feito:

# Importando a função choice do módulo random
from random import choice

# Lendo os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Colocando os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Escolhendo um aluno aleatoriamente
aluno_escolhido = choice(alunos)

# Mostrando o aluno escolhido
print("O aluno escolhido foi: {}".format(aluno_escolhido))


# Este programa pede ao usuário para inserir os nomes de quatro alunos. Esses nomes são armazenados em uma lista. Em seguida, o programa seleciona e imprime o nome de um aluno escolhido aleatoriamente da lista. A função choice() simplifica a seleção aleatória, tornando este programa uma solução eficaz para o problema proposto.

#_______________________________________________________________________________________________________________________________________________________________


# Para sortear a ordem de apresentação de trabalhos dos alunos, você pode usar a função shuffle() da biblioteca random, que reorganiza aleatoriamente os itens de uma lista. Dessa forma, depois de ler os nomes dos alunos, você pode embaralhar essa lista e então exibir a nova ordem. Aqui está como fazer isso:

# Importando a função shuffle do módulo random
from random import shuffle

# Lendo os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Colocando os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralhando a ordem dos alunos
shuffle(alunos)

# Mostrando a ordem sorteada
print("A ordem de apresentação será: ")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")


# Este programa primeiro coleta os nomes dos quatro alunos e os armazena em uma lista. Em seguida, ele usa shuffle() para embaralhar aleatoriamente essa lista, modificando a ordem dos alunos nela. Por fim, ele itera sobre a lista embaralhada, imprimindo a nova ordem de apresentação dos alunos. Note que a função shuffle() modifica a lista in-place, ou seja, altera a própria lista sem criar uma nova, o que é ideal para este caso de uso.
    
#_______________________________________________________________________________________________________________________________________________________________


# Para reproduzir um arquivo MP3 em Python, você pode usar a biblioteca pygame, que é amplamente utilizada para desenvolvimento de jogos, mas que também pode ser usada para tarefas multimídia, como reprodução de áudio.

import pygame
import sys

def play_music(mp3_file):
    # Inicializa o mixer de música do pygame
    pygame.mixer.init()
    # Carrega a música
    pygame.mixer.music.load(mp3_file)
    # Toca a música
    pygame.mixer.music.play()

    # Loop para manter a música tocando
    try:
        while pygame.mixer.music.get_busy():
            # Checa se o pygame está recebendo o evento QUIT (como fechar a janela)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
    except KeyboardInterrupt:
        # Para a música e fecha o programa se um KeyboardInterrupt (CTRL+C) ocorrer
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    mp3_file = 'C:\Users\stark\Music\Dragon Force\DragonForce-Heroes Of Our Time' # Substitua pelo caminho correto para o seu arquivo MP3
    play_music(mp3_file)

# Lembre-se de substituir 'caminho/para/seu/arquivo.mp3' pelo caminho correto do arquivo MP3 que você deseja reproduzir. Este programa inicializa o mixer do pygame, carrega o arquivo MP3, e começa a reproduzi-lo. Ele mantém a música tocando até que o arquivo termine ou o programa seja fechado, seja pelo usuário fechando a janela do programa (se houver uma) ou interrompendo o programa no terminal com um comando como CTRL+C.

# Se você encontrar algum problema para reproduzir o arquivo MP3 (como uma mensagem de erro indicando que o formato não é suportado), certifique-se de que o arquivo não está corrompido e que o pygame suporta o formato do arquivo. Embora o pygame geralmente suporte a reprodução de arquivos MP3, codecs específicos ou taxas de bits muito altas podem causar problemas.
    
#_______________________________________________________________________________________________________________________________________________________________
