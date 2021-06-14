#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e
#qual foi a soma entre elas (desconsiderando o flag).

#eu coloquei um verificador pra ver se o usuário inseriu apenas números hehe by: Maiyuri

c = soma = 0
while True:
    n = input("Insira um número [999 para parar]: ")
    if n.strip().isdigit():
        n = int(n)
        if n == 999:
            break
        else:
            soma = soma + n
            c = c + 1
    else:
        print("Por favor, digite somente números.")

print(f"Valor total da soma dos {c} números é de: {soma}")

