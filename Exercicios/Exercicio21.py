import pygame

pygame.init()
pygame.mixer.music.load('DragonForce2.mp3')
pygame.mixer.music.play()

# Loop para manter o programa rodando enquanto a música está tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
