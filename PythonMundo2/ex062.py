#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print("*" * 30)
print("10 primeiros termos de uma PA")
print("*" * 30)

primeiro_termo = int(input("Sua PA irá começar com qual número? "))
razao = int(input("Qual o intervalo dos números? "))
c = 1
qtd = 11

while c < qtd:
    calc = primeiro_termo + (c - 1) * razao
    print(calc, " -> ", end=" ")
    c = c + 1
p = -1
c2 = c
while p != 0:
    p = int(input('''Você gostaria de mostrar mais termos? Se sim, quantos? se não, insira o número 0.
Digite:'''))
    qtd = qtd + p
    if p != 0:
        while c2 < qtd:
            calc = primeiro_termo + (c2 - 1) * razao
            print(calc, " -> ", end=" ")
            c2 = c2 + 1
print("Acabou")