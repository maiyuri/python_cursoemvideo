#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
val = float(input("Qual o valor do produto?: R$"))
desconto = val - (val * 5 / 100)
print("O valor do seu produto R$ {:.2f} com o desconto de 5% é R$ {:.2f}.".format(val, desconto))
