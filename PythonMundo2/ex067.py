#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = 0
c = 0
while True:
    print("-"* 30)
    n = int(input('''Quer ver a tabuada de qual valor? 
(insira um valor menor que zero para parar o programa): '''))
    if n < 0:
        break
    if n > 0:
        for c in range(0,10):
            c = c + 1
            mult = n * c
            print(f"{n} X {c} = {mult}")
print("O programa acabou, obrigada!")
