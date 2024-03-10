**Roteiro de Aula para o Jogo da Forca em Python com Pygame**

# Introdução

## Boas-vindas

Olá alunos! Bem-vindos à nossa aula sobre como criar um jogo da forca em Python usando a biblioteca Pygame. Vamos explorar cada parte do código, entender como ele funciona e aprender a construir nosso próprio jogo.

---

# Etapa 1: Configuração Inicial

## Explicação do Código

```python
# Importação das Bibliotecas
import pygame
import sys
import random
import time

# Inicialização do Pygame
pygame.init()

# Configurações Iniciais
clock = pygame.time.Clock()
width = 800
height = 500

# Criação da Janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game")

# Ícone da Janela
icon = pygame.image.load("img_9.png")
pygame.display.set_icon(icon)
```

## Comentários

- Inicializamos o Pygame e configuramos a janela do jogo, definindo largura, altura e ícone.

---

# Etapa 2: Variáveis e Estruturas Iniciais

## Explicação do Código

```python
# Variáveis e Estruturas Iniciais
game_over = False
rows = 2
columns = 13
gap = 20
size = 40
boxes = []

for row in range(rows):
    for col in range(columns):
        x = ((col * gap) + gap) + (size * col)
        y = ((row * gap) + gap) + (size * row) + 330
        box = pygame.Rect(x, y, size, size)
        boxes.append(box)

buttons = []
A = 65

for index, box in enumerate(boxes):
    letter = chr(A + index)
    button = [box, letter]
    buttons.append(button)
```

## Comentários

- Definimos variáveis e estruturas iniciais para criar as caixas de letras que serão clicadas.

---

# Etapa 3: Função para Desenhar Botões

## Explicação do Código

```python
# Função para desenhar botões
def draw_buttons(buttons):
    for box, letter in buttons:
        btn_text = font.render(letter, True, (0, 0, 0))
        btn_rect = btn_text.get_rect(center=(box.x + 20, box.y + 20))
        screen.blit(btn_text, btn_rect)
        pygame.draw.rect(screen, (0, 0, 0), box, 2)
```

## Comentários

- Criamos uma função para desenhar os botões na tela com as letras correspondentes.

---

# Etapa 4: Função para Exibir a Palavra Oculta

## Explicação do Código

```python
# Função para exibir a palavra oculta
def display_guest():
    display_text = ''
    for letter in word:
        if letter in guessed:
            display_text += f'{letter} '
        else:
            display_text += '_ '

    text = letter_font.render(display_text, True, (0, 0, 0))
    screen.blit(text, (400, 200))
```

## Comentários

- Criamos uma função para exibir a palavra oculta com as letras adivinhadas.

---

# Etapa 5: Variáveis do Enforcado

## Explicação do Código

```python
# Variáveis do Enforcado
images = []
hangman_status = 0

words = ['PYGAME', 'PYTHON', 'JAVA', 'HELLO', 'WORLD', 
         'HANGMAN', 'TIME', 'TURTLE', 'RANDOM']
word = random.choice(words)
guessed = []
```

## Comentários

- Inicializamos variáveis para controlar o enforcado, escolhemos uma palavra aleatória e criamos uma lista para letras adivinhadas.

---

# Etapa 6: Loop Principal do Jogo

## Explicação do Código

```python
# Loop Principal do Jogo
running = True
while running:
    # Limpeza da Tela
    screen.fill((255, 255, 255))
```

## Comentários

- Iniciamos o loop principal do jogo, onde a tela é limpa a cada iteração.

---

# Etapa 7: Tratamento de Eventos

## Explicação do Código

```python
# Tratamento de Eventos
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        click_pos = event.pos

        for button, letter in buttons:
            if button.collidepoint(click_pos):
                if letter not in word:
                    hangman_status += 1

                if hangman_status == 6:
                    game_over = True

                guessed.append(letter)
                buttons.remove([button, letter])
```

## Comentários

- Verificamos eventos como clique do mouse ou fechamento da janela.

---

# Etapa 8: Exibição das Imagens do Enforcado

## Explicação do Código

```python
# Exibição das Imagens do Enforcado
for i in range(hangman_status):
    image = pygame.image.load(f"img_{21 + i}.png")
    images.append(image)

screen.blit(images[-1], (150, 150))
```

## Comentários

- Exibimos as imagens do enforcado conforme o status atual.

---

# Etapa 9: Desenho das Caixas e Palavra Oculta

## Explicação do Código

```python
# Desenho das Caixas e Palavra Oculta
for box in boxes:
    pygame.draw.rect(screen, (0, 0, 0), box, 2)
```

## Comentários

- Desenhamos as caixas e a palavra oculta na tela.

---

# Etapa 10: Verificação de Vitória ou Derrota

## Explicação do Código

```python
# Verificação de Vitória ou Derrota
won = True
for letter in word:
    if letter not in guessed:
        won = False

if won:
    game_over = True
    game_text = "YOU WIN!!!"
else:
    game_text = "OH NO, YOU LOST!!!"
```

## Comentários

- Verificamos se o jogador venceu ou perdeu.

---

# Etapa 11: Chamada de Funções de Desenho

## Explicação do Código

```python
# Chamada de Funções de Desenho
draw_buttons(buttons)
display_guest()
screen.blit(title_text, title_rect)
```

## Comentários

- Chamamos as funções de desenho para atualizar a tela.

---

# Etapa 12: Controle de Atualização e Tempo

## Explicação do Código

```python
# Controle de Atualização e Tempo
clock.tick(50)
pygame.display.update()
```

## Comentários

- Controlamos a atualização da tela e o tempo entre os frames.

---

# Etapa 13: Tela de Resultados

## Explicação do Código

```python
# Tela de Resultados
if game_over:
    screen.fill((255, 255, 255))
    text = game_font.render(game_text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()
```

## Comentários

- Exibimos a tela de resultados quando o jogo termina.

---

# Conclusão

## Recapitulação

Nesta aula, exploramos o código do jogo da forca em Python com Pygame, entendemos cada parte e aprendemos sobre eventos, gráficos e controle de fluxo.

## Prática

Agora, é hora de praticar! Tente modificar o código, adicionar novos recursos ou personalizar o jogo de acordo com suas ideias.

---

Espero que este roteiro ajude a conduzir uma aula envolvente sobre o desenvolvimento de jogos em Python usando Pygame!
