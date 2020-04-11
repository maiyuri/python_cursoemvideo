frase = input("Digite uma frase: ").strip()
qt_de_a = frase.upper().count("A")
primeira_posicao = frase.upper().find("A")+1
ultima_posicao = frase.upper().rfind("A")+1
print("A letra A aparece {} vezes.\n"
      "A primeira letra A apareceu na posição {}.\n"
      "A última letra A apareceu na posição {}.".format(qt_de_a, primeira_posicao, ultima_posicao))
