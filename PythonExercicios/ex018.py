#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, tan, sin, radians

ang = float(input("Digite o ângulo que você deseja: "))
rad = radians(ang)
seno = sin(rad)
coss = cos(rad)
tang = tan(rad)

print("O ângulo de {:.1f} tem o SENO de {:.2f}\n"
      "O ângulo de {:.1f} tem o COSSENO de {:.2f}\n"
      "O ângulo de {:.1f} tem o TANGENTE de {:.2f}".format(ang, seno, ang, coss, ang, tang))
