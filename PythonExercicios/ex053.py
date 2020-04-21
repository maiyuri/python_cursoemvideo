#Exercício Python 053: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase para verificar se ela é um palindromo: ").upper()
conta = len(frase)
for c in range(1):
    tiraespaco = frase.replace(" ", "")
    tiraespacos = frase.strip()
    invertida = tiraespaco[::-1]
    if invertida == tiraespaco:
        print("A Frase {} é palíndromo, pois ela invertida é {}.".format(tiraespacos, invertida))
    else:
        print("A frase {} não é palíndromo, pois ela invertida é {}.".format(tiraespacos, invertida))
