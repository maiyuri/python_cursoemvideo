#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print("*" * 30)
print("10 primeiros termos de uma PA")
print("*" * 30)

primeiro_termo = int(input("qUALÉ? primeiro termo: "))
razao = int(input("razionnn?"))

for c in range(1, 11):
    calc = primeiro_termo + (c - 1) * razao
    print(calc," -> ", end=" ")
print("Acabou")
