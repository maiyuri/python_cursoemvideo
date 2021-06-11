# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao to do (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input("Qual o seu nome completo?"))
maiusculo = nome.upper()
minusculo = nome.lower()
separado = nome.split()
total_letras = len(nome.replace(" ", ""))
primeiro_nome = separado[0].capitalize()
total_letras_primeiro_nome = len(primeiro_nome)

print("""Analisando o seu nome..
        Seu nome em letra maiúsculas é {}
        Seu nome em letra minúscula é {}
        Seu nome tem ao todo tem {} letras
        Seu primeiro nome é {} e tem {} letras""".format(maiusculo, minusculo, total_letras, primeiro_nome,
                                                         total_letras_primeiro_nome))
