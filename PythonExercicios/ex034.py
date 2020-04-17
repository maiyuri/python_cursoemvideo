#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input("Informe o seu salário para verificarmos quanto de aumento você ira ter: R$"))

if salario > 1250:
    novo_salario = salario + (salario * 0.10)
    print("O seu salário era de R${:.2f} e agora com o aumento de 10% é de R${:.2f}".format(salario, novo_salario))
else:
    novo_salario_2 = salario + (salario * 0.15)
    print("O seu salário era de R${:.2f} e agora com o aumento de 15% é de R${:.2f}".format(salario, novo_salario_2))
#--------------------------

padrao = 0.15

if salario > 1250:
    padrao = 0.10
novo_salario = salario + (salario * padrao)
print("O seu salário era de R${:.2f} e agora com o aumento de {:.0f}% é de R${:.2f}".format(salario, (padrao * 100), novo_salario))





