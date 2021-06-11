#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("*" * 30)
print("10 primeiros termos de uma PA")
print("*" * 30)

primeiro_termo = int(input("Sua PA irá começar com qual número? "))
razao = int(input("Qual o intervalo dos números? "))
c = 0

while c < 10:
    calc = primeiro_termo + (c - 1) * razao
    print(calc, " -> ", end=" ")
    c = c + 1
print("Acabou")