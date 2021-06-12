#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

import math

num = int(input('''Por favor, insira um número e eu calcularei o fatorial dele
numero: '''))
n = num
calc_fatorial = math.factorial(num)
print("{}! = ".format(num), end='')

while n > 0:
    print('{}'.format(n), end='')
    if n > 1:
        print('x', end='')
    elif n == 1:
        print(' = {} '.format(calc_fatorial), end='')
    n = n - 1