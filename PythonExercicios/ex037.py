#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.


numeroint = int(input("Olá! escreva um número inteiro: "))
escolhanumero = int(input("Agora escolha uma opção de conversão desse número:\n"
                          "- 1 para binário\n"
                          "- 2 para octal\n"
                          "- 3 para hexadecimal: "))

if escolhanumero == 1:
    numbinario = bin(numeroint)[2:]
    print(numbinario)
elif escolhanumero == 2:
    numoctal = oct(numeroint)[2:]
    print(numoctal)
elif escolhanumero == 3:
    numhexa = hex(numeroint)[2:]
    print(numhexa)
else:
    print("Opção inválida, tente novamente.")
