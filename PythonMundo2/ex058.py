#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

numerpc = randint(1, 10) #computador sorteando o número
tentativas = 1
numerouser = 0

print('Tente adivinhar o número que o pc ira sortear e ganhe um premio !! obs: de 1 á 10: ')
numerouser = int(input('Insira o número: '))

while numerpc != numerouser:
    tentativas = tentativas + 1
    numerouser = int(input('Errou, tente novamente: '))

print("PROCESSANDO...")
sleep(2)
print("Você venceu, o número é {} e você precisou de {} tentativas para acertar! :)".format(numerpc, tentativas))


