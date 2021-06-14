# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
val_total = 0
cont_mil = 0
menor_val = 0
c = 0

print("=" * 30)
print("       Mercadinho da ZL   ")
print("=" * 30)
while True:
    nome_prod = input("Nome do produto: ")
    preco_prod = float(input("Preço: R$"))
    cont = input("Deseja continuar? [S/N]: ").strip().upper()
    c = c + 1
    val_total = val_total + preco_prod
    if preco_prod > 1000:
        cont_mil = cont_mil + 1
    if c == 1 or preco_prod < menor_val:
        menor_val = preco_prod
        prod_menor_val = nome_prod
    if cont == "N":
        break

print(f'''A) qual é o total gasto na compra: R${round(val_total, 2)}
B) quantos produtos custam mais de R$1000: {cont_mil}
C) qual é o nome do produto mais barato: {prod_menor_val} que foi de R${round(menor_val, 2)}''')
