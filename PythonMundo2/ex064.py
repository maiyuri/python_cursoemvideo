#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
c = 0
n2 = 0
while n != 999:
    n = int(input("Insira um número: "))
    result = n + n2
    n2 = result
    c = c + 1
resultfinal = result - 999
c1 = c - 1
print("O resultado da soma dos números que você inseriu é de: {} e você inseriu {} números.".format(resultfinal, c1))