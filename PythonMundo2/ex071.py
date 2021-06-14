#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
#vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 30)
print("       Banco da Perifa     ")
print("=" * 30)

saque = None
saquedividido = saque
while True:
    saque = int(input("Qual o valor que você deseja sacar?: "))
    if saque % 50 == 0:
        divisao = int(saque / 50)
        print(f"Será entregue {divisao} notas de 50 reais cada uma.")
    elif saque % 20 == 0:
        divisao = int(saque / 20)
        print(f"Será entregue {divisao} notas de 20 reais cada uma.")
    elif saque % 10 == 0:
        divisao = int(saque / 10)
        print(f"Será entregue {divisao} notas de 10 reais cada uma.")
    novosaque = input("Gostaria de sacar mais dinheiro? [S/N]: ").upper()[0]
    if novosaque == "N":
        break