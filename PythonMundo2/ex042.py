#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes



print("me informe o comprimento de 3 retas e eu irei verificar se elas podem ou não formar um triângulo.")
lado1 = float(input("Primeira reta: "))
lado2 = float(input("Segunda reta: "))
lado3 = float(input("Terceira reta: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Pode ser triangulo!")
    if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
        print("Esse é um triangulo equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Esse é um triangulo Isósceles")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("Esse é um triangulo escaleno")
else:
    print("Com essas medidas, não é possivel fazer um triangulo!")



