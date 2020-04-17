#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
anonasc = int(input("Em que ano você nasceu? "))
idade = date.today().year - anonasc

if idade <= 9:
    print("Até 9 anos, Mirim")
elif idade > 9 and idade <= 14:
    print("Até 14 anos, Infantil")
elif idade > 14 and idade <= 19:
    print("Até 19 anos, Junior")
elif idade > 19 and idade <= 25:
    print("Até 25 anos, Sênior")
elif idade > 25:
    print("Acima de 25 anos, Master")
