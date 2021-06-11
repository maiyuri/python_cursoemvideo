#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Salario inicial: "))
aumento = salario + (salario * 15 / 100)

print("Seu salário de {:.2f} após o ajuste será de {:.2f}".format(salario, aumento))
