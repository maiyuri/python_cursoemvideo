nome = input("Qual o seu nome completo? ").strip()
separado = nome.split()
primeiro_nome = separado[0]
ultimo_nome = separado[-1]
ultimo_nome_2 = separado[len(separado) - 1]
print("Primeiro nome: {}\n"
      "Ultimo nome: {}".format(primeiro_nome, ultimo_nome))
