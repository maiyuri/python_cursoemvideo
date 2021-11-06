#Exercício Python #078 - Maior e Menor valores na Lista
list = []
indmaior = []
indmenor = []
maior = None
menor = None
for i in range(0, 5):
    val = int(input(f"Digite um valor para a Posição {i}: "))
    list.append(val)
    if maior is None or val > maior:
        maior = val

    if menor is None or val < menor:
        menor = val

print("=-"*20)
print("Você digitou os valores", list)

for ind, val in enumerate(list):
    if val == maior:
        indmaior.append(ind)
    if val == menor:
        indmenor.append(ind)

print(f"O maior valor digitado foi {maior} nas posições", end='')
for v in indmaior:
    print(f" {v}...", end='')

print(f"\nO menor valor digitado foi {menor} na posições", end='')
for v in indmenor:
    print(f" {v}...", end='')