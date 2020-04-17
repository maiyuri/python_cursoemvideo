#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = float(input("Com quantos km/h você passou?"))
calc_multa = (velocidade_carro - 80) * 7
if velocidade_carro > 80:
    print("""Você sera multado por passar da velocidade de 80km/h, cada kilomêtro passado é cobrado o valor de R$7, 
logo o valor total da multa é de {} reais.""".format(calc_multa))
else:
    print("Parabéns, você não levará multa, pois passou abaixo de 80km/h")