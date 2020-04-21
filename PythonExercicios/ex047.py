#Exercício Python 047: Crie um programa que mostre na tela
#todos os números pares que estão no intervalo entre 1 e 50.
print("Esses sao os numeros pares de 1 á 50: ")
for contador in range(1, 51):
    par = contador % 2
    if par == 0:
        print(contador)
print("Acabou")