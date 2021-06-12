#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print('*'*30)
n1 = int(input('''Insira um número e eu darei a sequência fibonacci.
Digite: '''))
print('*'*30)

c = 3
f1 = 0
f2 = 1
f = 3
print(f1," -> ", f2, end=" ")
while c <= n1:
    f = f1 + f2
    c = c + 1
    f1 = f2
    f2 = f
    print(" -> ", f, end=" ")
print(" -> Acabou")
