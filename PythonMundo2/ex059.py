#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

print('Olá! eu sou uma calculadora, insira dois números:')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
menu = 0

while menu != 5:
    menu = int(input('''
Qual operação você deseja realizar?
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
Número: '''))
    if menu == 1:
        soma = num1 + num2
        print("A soma do número {} e {} é igual a {}".format(num1, num2, soma))
    elif menu == 2:
        mult = num1 * num2
        print("A multiplicação dos números {} e {} é igual a {}".format(num1, num2, mult))
    elif menu == 3:
        if num1 > num2:
            print("O número {} é maior que o número {}.".format(num1, num2))
        elif num2 < num1:
            print("O número {} é maior que o número {}.".format(num2, num1))
        elif num1 == num2:
            print("Os números são exatamente iguais!")
    elif menu == 4:
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    else:
        print("Opção inválida, tente novamente.")

