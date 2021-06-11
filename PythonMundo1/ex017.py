#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import sqrt, hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

calculoNaMao = sqrt((co ** 2) + (ca ** 2))
calculoHypot = hypot(co, ca)

print("A hipotenusa vai medir {:.2f}".format(calculoNaMao))
print("A hipotenusa vai medir {:.2f}".format(calculoHypot))
