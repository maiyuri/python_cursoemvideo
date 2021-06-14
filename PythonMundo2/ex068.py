#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
#consecutivas que ele conquistou no final do jogo.
import random
from time import sleep
somacont = 0
while True:
    print("*" * 30)
    opcao_user = input("Par ou ímpar? [P/I]: ").strip().upper()[0]
    print("Jó..")
    sleep(2)
    print("Ken..")
    sleep(2)
    print("Pô..")
    n = int(input("Insira seu número: "))
    pc = random.randrange(10)
    print("Número do pc:", pc)
    soma = n + pc
    if soma % 2 == 0 and opcao_user == "I":
        print(f"o número {soma} é ímpar e você escolheu par, eu ganhei! HAHAHAH")
        break
    elif soma % 2 == 1 and opcao_user == "P":
        print(f"o número {soma} é par e você escolheu ímpar, eu ganhei! HAHAHAH")
        break
    elif soma % 2 == 0 and opcao_user == "P":
        print(f"o número {soma} é par, você ganhou >.>")
        somacont = somacont + 1
    elif soma % 2 == 1 and opcao_user == "I":
        print(f"o número {soma} é ímpar, você ganhou >.>")
        somacont = somacont + 1
    cont = input("Deseja continuar? [s/n]: ").strip().upper()[0]
    if cont == "N":
        break

print(f"Game Over, você ganhou {somacont} vezes seguidas.")

