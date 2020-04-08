# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
num = int(input("Digite um número para ver a sua tabuada: "))

print('-' * 12)
for tabuada in range(1, 11):
    print("{} x {:2} = {}".format(num, tabuada, num * tabuada))
print('-' * 12)
