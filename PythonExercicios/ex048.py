#Faça um programa que calcule a soma
#entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
contador = 0
soma = 0
for c in range(1, 501):
    impar = c % 2
    mult_tres = c % 3
    if impar == 1 and mult_tres == 0:
        soma = soma + c
        contador = contador + 1

print("A soma dos {} valores é {}.".format(contador, soma))


