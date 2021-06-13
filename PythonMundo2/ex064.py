#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = int(input("Insira um número: "))
c = 0
result = 0
while n != 999:
    result = result + n
    c += 1
    n = int(input("Insira um número: "))
print("O resultado da soma dos números que você inseriu é de: {} e você inseriu {} números.".format(result, c))