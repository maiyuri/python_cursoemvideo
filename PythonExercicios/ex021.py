#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# Importando o PyGame

import pygame

# Inicializando o PyGame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
