#Exercício Python 074: Crie um programa que vai gerar cinco números
#aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
#números gerados e também indique o menor e o maior valor que estão na tupla.
import random as r
tupla = tuple()
maior = 0
menor = None
for i in range(0, 5):
    num_aleatorio = r.randint(1, 99)
    if num_aleatorio > maior:
        maior = num_aleatorio
    if menor is None or num_aleatorio < menor:
        menor = num_aleatorio
    num_aleatorio = tuple([num_aleatorio])
    tupla = tupla + num_aleatorio

    
print(tupla, f'O menor número é: {menor} e o maior é: {maior}')
