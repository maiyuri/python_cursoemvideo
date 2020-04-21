#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada
#   de um número que o usuário escolher, só que agora utilizando um laço for.

print("------Tabuada-------")
num_tabuada = int(input("Por favor, insira um número que você deseja ver a tabuada: "))
for c in range(0, 11):
    calc = num_tabuada * c
    print("{} x {} = {}".format(num_tabuada, c, calc))
