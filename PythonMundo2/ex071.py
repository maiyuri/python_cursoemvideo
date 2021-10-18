#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
#vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 30)
print("       Banco da Perifa     ")
print("=" * 30)

saque = None
divisao_nota_50 = 0
divisao_nota_20 = 0
divisao_nota_10 = 0
divisao_nota_5 = 0
while True:
    saque = int(input("Qual o valor que você deseja sacar?: "))
    if saque >= 50:
        divisao_nota_50 = int(saque / 50)
        saque = saque - (divisao_nota_50 * 50)

    if saque >= 20:
        divisao_nota_20 = int(saque / 20)
        saque = saque - (divisao_nota_20 * 20)

    if saque >= 10:
        divisao_nota_10 = int(saque / 10)
        saque = saque - (divisao_nota_10 * 10)

    if saque >= 5:
        divisao_nota_5 = int(saque / 5)
        saque = saque - (divisao_nota_5 * 5)

    print(f'Será entregue {divisao_nota_50} notas de 50\n' 
          f'{divisao_nota_20} notas de 20\n'
          f'{divisao_nota_10} notas de 10\n'
          f'{divisao_nota_5} notas de 5. ')
    novosaque = input("Gostaria de sacar mais dinheiro? [S/N]: ").upper()[0]
    if novosaque == "N":
        break