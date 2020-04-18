from time import sleep
import emoji
import pygame
import os

for c in range(10, 0 , -1):
    print(c)
    sleep(1)

print(emoji.emojize( ' * Fogos estourando * :collision: /play trombone'  ,use_aliases=True))

pygame.init()

if os.path.exists('musica.mp3'):
    pygame.mixer.init()
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play()

else:
    print('O arquivo musica.mp3 não está no diretório do script Python')

