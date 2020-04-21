maisvelho = 0
nomevelho = ''
media = 0
somaidade = 0
qtdmulher = 0
for c in range(1, 5):
    print("=" * 5, "{} pessoa".format(c), "=" * 5)
    nome = input("Qual o seu nome? ").strip()
    idade = int(input("Qual a sua idade? "))
    sexo = input("Você é um homem ou uma mulher? [M/F]:  ").strip().upper()
    somaidade += idade
    media = somaidade / c

    if sexo == "M" and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome

    if sexo == "F" and idade < 20:
        qtdmulher += 1

print("O hmem mais velho é {} com a idade de {}.".format(nomevelho, maisvelho))
print("A média de idade é {}".format(media))
print("O número de mulheres abaixo de 20 anos é {}.".format(qtdmulher))
