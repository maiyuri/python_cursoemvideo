#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input("Você é do sexo F ou M? [F/M] ").upper()
while sexo != "F" and sexo != "M":
    print("Digite sexo válido!")
    sexo = input("Você é do sexo F ou M? [F/M] ").upper()

print("Sexo válido, muito obrigado!")
