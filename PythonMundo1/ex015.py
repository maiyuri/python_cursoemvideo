#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos km esse carro percorreu? "))
dia = int(input("Por quantos dias você ficou com o carro? "))
val_km = km * 0.15
val_dia = dia * 60.00
total = val_km + val_dia

print("valor total a pagar é {:.2f}".format(total))
