n = 0
c = 0
n2 = 0
while n != 999:
    n = int(input("Insira um número: "))
    result = n + n2
    n2 = result
    c = c + 1
resultfinal = result - 999
c1 = c - 1
media = round(resultfinal / c1, 2)
print("O resultado da soma dos números que você inseriu é de: {} e você inseriu {} números e a media dos valores é de {}.".format(resultfinal, c1, media))