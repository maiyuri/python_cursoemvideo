import random
import time

lista = ["pedra", "papel", "tesoura"]

jokempo = int(input("Vamos jogar jokenpô?\n"
                "Escolha um:\n"
                "[1] Pedra\n"
                "[2] Papel\n"
                "[3] Tesoura\n"
                "Sua escolha: "))

time.sleep(1)
print("Jokeeee", end="")
time.sleep(1)
print("eeeem", end="")
time.sleep(1)
print("pô!")
time.sleep(0.5)


sorteio = random.randint(1, 3)

print("--------------------------")
if sorteio == jokempo:
    print("Ops deu empate!!")
elif sorteio == 1 and jokempo == 2:
    print("Ihhuuu você venceu!")
elif sorteio == 2 and jokempo == 3:
    print("Você ganhou!")
elif sorteio == 3 and jokempo == 1:
    print("Você ganhou >.>")
else:
    print("eu ganhei HAHAHAHAHA")


print("--------------------------")
print("Máquina escolheu {}".format(lista[sorteio - 1]))



