#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

num = float(input("Quantos km você gastou na sua viagem? "))

if num <= 200:
    calc_viagem = num * 0.50
    print("O valor total a ser cobrado pela viagem é de {:.2f}".format(calc_viagem))
else:
    calc_viagem_mais = num * 0.45
    print("O valor total a ser cobrado pela sua viagem é de {:.2f}".format(calc_viagem_mais))

