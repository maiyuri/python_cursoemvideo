din = float(input("Quanto dinheiro você tem na carteira? R$"))
cambio = din / 5.29

print("Com R${} você pode comprar US${:.2f}".format(din, cambio))
