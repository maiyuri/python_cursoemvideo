#Faça um programa que leia algo pelo teclado o seu tipo primitivo e todas as infomações possiveis sobre ele

algo = input("Digite algo: ")

print("O tipo do seu valor é", type(algo),
      "\nÉ tudo minúsculo?", algo.islower(),
      "\nÉ um título?", algo.istitle(),
      "\nÉ tudo maiusculo?", algo.isupper(),
      "\nÉ decimal?", algo.isdecimal(),
      "\nÉ string? ", algo.isalpha(),
      "\nÉ numerico?", algo.isnumeric())
