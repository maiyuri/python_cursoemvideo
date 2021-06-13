n = int(input("Insira um número: "))
c = 0
result = 0
maior = 0
menor = None
while n != 999:
    result = result + n
    c += 1
    if n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n
    n = int(input("Insira um número [Para parar o programa digite 999]: "))

print('''O resultado da soma dos números que você inseriu é de: {} e você inseriu {} números.
E o maior número é {}
E o menor número é {}'''.format(result, c, maior, menor))
