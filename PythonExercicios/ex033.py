#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("Me fale 3 números e irei dizer qual deles é maior e qual é o menor: ")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O maior número é o {}".format(num1))
elif num2 > num1 and num2 > num3:
    print("O maior número é o {}".format(num2))
elif num3 > num2 and num3 > num1:
    print("O maior número é o {}".format(num3))

if num1 < num2 and num1 < num3:
    print("O menor número é o {}".format(num1))
elif num2 < num1 and num2 > num3:
    print("O menor número é o {}".format(num2))
elif num3 < num2 and num3 > num1:
    print("O menor número é o {}".format(num3))
