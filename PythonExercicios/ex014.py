# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Qual a temperatura em Cº?"))
f = (c * 9/5) + 32

print("Cº {} Fº {} ".format(c, f))