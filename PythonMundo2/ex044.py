#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto

preconormal = float(input("Qual o preço normal do produto?"))
formadepagamento = int(input("""Qual a forma de pagamento?

1: Á vista dinheiro/cheque
2: Á vista no cartão
3: Em até 2x no cartão 
4: 3x ou mais no cartão\n"""))


if formadepagamento == 1:
    desconto = preconormal - (preconormal * 0.10)
    print("Essa forma de pagamento te dá desconto de 10%, logo o valor total a pagar é de {}.".format(desconto))
elif formadepagamento == 2:
    desconto = preconormal - (preconormal * 0.05)
    print("Essa forma de pagamento te dá desconto de 5%, logo o valor total a pagar é de {}.".format(desconto))
elif formadepagamento == 3:
    print("Essa forma de pagamento não te dá nenhum desconto, logo o valor total a pagar é o valor real do produto {}".format(preconormal))
elif formadepagamento == 4:
    juros = preconormal + (preconormal * 0.20)
    print("Essa forma de pagamento cobra 20% de juros em cima do valor normal, valor total de {}.".format(juros))
