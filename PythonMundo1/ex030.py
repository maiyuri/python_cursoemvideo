#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Me fale um número: "))
par_ou_impar = num % 2

if par_ou_impar == 0:
    print("O seu número é par! ")
else:
    print("O seu número é ímpar! ")