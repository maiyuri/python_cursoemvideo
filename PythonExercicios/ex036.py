#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a
# compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


val_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o valor do salário? R$"))
anos = int(input("Em quantos anos você vai pagar? "))

calc = val_casa / anos
trinta_por_cento = salario * 0.30

if calc > trinta_por_cento:
    print("O seu emprestimo foi negado.")
else:
    print("Seu emprestimo foi aprovado!")