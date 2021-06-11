#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
somamaior = 0
somamenor = 0
for c in range(1, 8):
    anonasci = int(input("Em que ano você nasceu? "))
    idade = date.today().year - anonasci
    if idade < 18:
        somamenor = somamenor + 1
    elif idade >= 18:
        somamaior = somamaior + 1
print("O número de pessoas de menor é {}.".format(somamenor))
print("O número de pessoas de maior é {}.".format(somamaior))
