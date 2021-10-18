#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
#por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
#mostrá-lo por extenso.

numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
                  'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                  'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num > 20:
        print("Por favor, insira um número menor.")
    elif num < 0:
        print("Por favor, insira um número maior.")
    else:
        print(f'Você Digitou o número {numero_extenso[num]}.')

    resp = input('Você gostaria de colocar mais algum número?').upper()

    if resp == 'N':
        break
print("Ok, acabou o programa, volte sempre!")