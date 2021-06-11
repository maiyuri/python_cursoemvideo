#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from time import sleep
from datetime import date
ano = int(input("Quer descobrir se o ano que você escrever é bissexto? é só escrever ele ai, caso"
                "queira saber sobre o ano atual, digite 0: "))
data_atual = date.today()
data_em_texto = data_atual.strftime('%Y') #ou date.today().year

print("Analisando.", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".")
sleep(0.5)

if ano == 0:
    ano = int(data_em_texto)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Esse ano de {} é bissexto!".format(ano))
else:
    print("Esse ano de {} não é bissexto!".format(ano))

