#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print("*" * 30)
print("10 primeiros termos de uma PA")
print("*" * 30)

primeiro_termo = int(input("Sua PA irá começar com qual número? "))
razao = int(input("Qual o intervalo dos números? "))
c = 0
p = -1
c2 = 0
while c < 10:
    calc = primeiro_termo + (c - 1) * razao
    print(calc, " -> ", end=" ")
    c = c + 1

while p != 0:
    p = input("Você gostaria de mostrar mais termos? Se sim, quantos? se não, insira o número 0.")
    if p != 0:
        while c2 < 10:
            calc = primeiro_termo + (c - 1) * razao
            print(calc, " -> ", end=" ")
            c = c + 1
print("Acabou")