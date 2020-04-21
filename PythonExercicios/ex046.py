#Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva
#para o estouro de fogos de artifício, indo de 10 até 0,
#com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print(emoji.emojize( ' * Fogos estourando * :collision: /play trombone', use_aliases=True))

