#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
masc = 0
fem = 0
maisdezoito = 0

print("Esse é um programa que cadastra pessoas.")
while True:
    idade = int(input("Qual a idade da pessoa?: ").strip())
    sexo = input("Qual o sexo da pessoa? [M/F]: ").strip().upper()[0]
    cont = input("Gostaria de continuar? [S/N]: ").strip().upper()[0]
    print("*" * 30)
    if sexo == "F" and idade <= 20:
        fem = fem + 1
    if sexo == "M":
        masc = masc + 1
    if idade >= 18:
        maisdezoito = maisdezoito + 1
    if cont == "N":
        break

print(f'''A) quantas pessoas tem mais de 18 anos: {maisdezoito}
B) quantos homens foram cadastrados: {masc}
C) quantas mulheres tem menos de 20 anos: {fem}''')
