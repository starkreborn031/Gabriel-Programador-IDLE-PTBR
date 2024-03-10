import pygame
import sys
import random
import time

pygame.init()

# Configurações iniciais
clock = pygame.time.Clock()
largura = 800
altura = 500

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Forca")

# Variáveis do jogo
fim_de_jogo = False
linhas = 2
colunas = 13
espacamento = 20
tamanho = 40
caixas = []

for linha in range(linhas):
    for coluna in range(colunas):
        x = ((coluna * espacamento) + espacamento) + (tamanho * coluna)
        y = ((linha * espacamento) + espacamento) + (tamanho * linha) + 330
        caixa = pygame.Rect(x, y, tamanho, tamanho)
        caixas.append(caixa)

botoes = []
A = 65

for indice, caixa in enumerate(caixas):
    letra = chr(A + indice)
    botao = [caixa, letra]
    botoes.append(botao)

# Função para desenhar os botões
def desenhar_botoes(botoes):
    for caixa, letra in botoes:
        texto_botao = fonte.render(letra, True, (0, 0, 0))
        retangulo_botao = texto_botao.get_rect(center=(caixa.x + 20, caixa.y + 20))
        tela.blit(texto_botao, retangulo_botao)
        pygame.draw.rect(tela, (0, 0, 0), caixa, 2)

# Função para exibir a palavra oculta
def exibir_palavra_oculta():
    texto_exibicao = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            texto_exibicao += f'{letra} '
        else:
            texto_exibicao += '_ '

    texto = fonte_letra.render(texto_exibicao, True, (0, 0, 0))
    tela.blit(texto, (400, 200))

# Variáveis do enforcado
partes_enforcado = 0
posicao_enforcado = [(400, 150), (400, 180), (400, 210), (400, 240), (390, 180), (410, 180)]

fonte = pygame.font.SysFont("arial", 30)
fonte_jogo = pygame.font.SysFont("arial", 80)
fonte_letra = pygame.font.SysFont("arial", 60)

titulo = "Jogo da forca"
texto_titulo = fonte_jogo.render(titulo, True, (0, 0, 0))
retangulo_titulo = texto_titulo.get_rect(center=(largura // 2, texto_titulo.get_height() // 2 + 10))

# Lista de palavras
palavras = ['PYGAME', 'PYTHON', 'JAVA', 'HELLO', 'WORLD', 
            'HANGMAN', 'TIME', 'TURTLE', 'RANDOM']
palavra = random.choice(palavras)
letras_adivinhadas = []

# Loop principal do jogo
executando = True
while executando:

    tela.fill((255, 255, 255))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicao_clicada = evento.pos

            for botao, letra in botoes:
                if botao.collidepoint(posicao_clicada):
                    if letra not in palavra:
                        partes_enforcado += 1

                    if partes_enforcado == 6:
                        fim_de_jogo = True

                    letras_adivinhadas.append(letra)
                    botoes.remove([botao, letra])

    # Desenhando o enforcado
    for i in range(partes_enforcado):
        pygame.draw.circle(tela, (0, 0, 0), posicao_enforcado[i], 20)

    for caixa in caixas:
        pygame.draw.rect(tela, (0, 0, 0), caixa, 2)

    venceu = True
    for letra in palavra:
        if letra not in letras_adivinhadas:
            venceu = False

    if venceu:
        fim_de_jogo = True
        texto_jogo = "VOCÊ VENCEU!!!"
    else:
        texto_jogo = "IXI, VOCÊ PERDEU!!!"

    desenhar_botoes(botoes)
    exibir_palavra_oculta()
    tela.blit(texto_titulo, retangulo_titulo)
    clock.tick(50)
    pygame.display.update()

    # Tela de Resultados
    if fim_de_jogo:
        tela.fill((255, 255, 255))
        texto_resultado = fonte_jogo.render(texto_jogo, True, (0, 0, 0))
        retangulo_resultado = texto_resultado.get_rect(center=(largura // 2, altura // 2))
        tela.blit(texto_resultado, retangulo_resultado)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

pygame.quit()
