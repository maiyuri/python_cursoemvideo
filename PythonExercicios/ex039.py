#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
ano_nascimento = int(input("Em que ano você nasceu?"))
idade = date.today().year - ano_nascimento

if idade <= 17:
    idadeatual = 18 - idade
    print("Você ainda irá se alistar ao serviço militar e falta {} ano(s) para você se alistar".format(idadeatual))
elif idade == 18:
    print("É a hora de se alistar ao serviço militar")
elif idade > 18:
    idadeatual = idade - 18
    print("Já passou {} anos do tempo de se alistar".format(idadeatual))
