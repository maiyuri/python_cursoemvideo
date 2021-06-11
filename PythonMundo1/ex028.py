#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um
#número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
#número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
numerpc = randint(0, 5) #computador sorteando o número
numerouser = int(input("Tente adivinhar o número que o pc ira sortear e ganhe um premio !! obs: de 0 á 5: "))

print("PROCESSANDO...")
sleep(2)
if numerouser == numerpc:
    print("Você venceu, o número é {}".format(numerpc))
else:
    print("infelizmente voce perdeu, o número é {}".format(numerpc))

