#Exercício Python016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import floor
num = float(input("Digite um valor: "))
inteiro = floor(num)

print("O valor digitado foi o {} e a sua porção inteira é {}".format(num, inteiro))
