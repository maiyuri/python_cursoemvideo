nome = input("Qual o seu nome? ").strip()
maiusculo = nome.upper()
sobrenome = nome.upper().__contains__("SILVA")
print("SILVA" in maiusculo)
