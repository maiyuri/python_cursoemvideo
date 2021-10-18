#Exercício Python 075: Desenvolva um programa que
#leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
num_nove = 0
pares = tuple()
posicao_num = None
tupla = tuple()


for i, z in enumerate(range(0, 4)):
    num = int(input("Por favor, insira um número: "))
    num_tuple = tuple([num])
    if num % 2 == 0:
        pares = pares + num_tuple
    tupla = tupla + num_tuple

if 3 in tupla:
    posicao_num = tupla.index(3)
    posicao_num = str(posicao_num + 1)
    num_tres_posi = posicao_num + '° posição.'
else:
    num_tres_posi = 'não possui número 3 na lista.'

num_nove = str(tupla.count(9)) + ' vezes.' if 9 in tupla else 'não possui número 9 na lista.'


print(f"Os números digitados foram: {tupla}\n"
      f"A) Quantas vezes apareceu o valor 9: {num_nove}\n"
      f"B) Em que posição foi digitado o primeiro valor 3: {num_tres_posi}\n"
      f"C) Quais foram os números pares: {pares}")



