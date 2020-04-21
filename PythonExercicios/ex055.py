#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input("Qual o seu peso? "))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print("O maior peso inserido foi {} e o menor foi {}.".format(pesomaior, pesomenor))
