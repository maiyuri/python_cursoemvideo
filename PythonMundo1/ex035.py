#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.
print("\033[1;35;40m*-*\033[m"*20) #cores
print("me informe o comprimento de 3 retas e eu irei verificar se elas podem ou não formar um triângulo.")
lado1 = float(input("Primeira reta: "))
lado2 = float(input("Segunda reta: "))
lado3 = float(input("Terceira reta: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Pode ser triangulo!")
else:
    print("Com essas medidas, não é possivel fazer um triangulo!")



