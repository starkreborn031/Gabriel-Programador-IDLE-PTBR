import pygame
import sys
import random
import time

pygame.init()

# Initial settings
clock = pygame.time.Clock()
width = 800
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game")

icon = pygame.image.load("img_9.png")
pygame.display.set_icon(icon)

# Game variables
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

# Function to draw buttons
def draw_buttons(buttons):
    for box, letter in buttons:
        btn_text = font.render(letter, True, (0, 0, 0))
        btn_rect = btn_text.get_rect(center=(box.x + 20, box.y + 20))
        screen.blit(btn_text, btn_rect)
        pygame.draw.rect(screen, (0, 0, 0), box, 2)

# Function to display the hidden word
def display_guest():
    display_text = ''
    for letter in word:
        if letter in guessed:
            display_text += f'{letter} '
        else:
            display_text += '_ '

    text = letter_font.render(display_text, True, (0, 0, 0))
    screen.blit(text, (400, 200))

# Hangman variables
images = []
hangman_status = 0

words = ['PYGAME', 'PYTHON', 'JAVA', 'HELLO', 'WORLD', 
         'HANGMAN', 'TIME', 'TURTLE', 'RANDOM']
word = random.choice(words)
guessed = []

font = pygame.font.SysFont("arial", 30)
game_font = pygame.font.SysFont("arial", 80)
letter_font = pygame.font.SysFont("arial", 60)

title = "Hangman Game"
title_text = game_font.render(title, True, (0, 0, 0))
title_rect = title_text.get_rect(center=(width // 2, title_text.get_height() // 2 + 10))

# Main game loop
running = True
while running:

    screen.fill((255, 255, 255))

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

    # Displaying the images accordingly
    for i in range(hangman_status):

        if i == 1:
            image = pygame.image.load("img_22.png")
            images.append(image)
        elif i == 2:
            image = pygame.image.load("img_23.png")
            images.append(image)
        elif i == 3:
            image = pygame.image.load("img_24.png")
            images.append(image)
        elif i == 4:
            image = pygame.image.load("img_25.png")
            images.append(image)
        elif i == 5:
            image = pygame.image.load("img_26.png")
            images.append(image)

    screen.blit(images[-1], (150, 150))

    for box in boxes:
        pygame.draw.rect(screen, (0, 0, 0), box, 2)

    won = True
    for letter in word:
        if letter not in guessed:
            won = False

    if won:
        game_over = True
        game_text = "YOU WIN!!!"
    else:
        game_text = "OH NO, YOU LOST!!!"

    draw_buttons(buttons)
    display_guest()
    screen.blit(title_text, title_rect)
    clock.tick(50)
    pygame.display.update()

    # Results screen
    if game_over:

        screen.fill((255, 255, 255))
        text = game_font.render(game_text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

pygame.quit()
