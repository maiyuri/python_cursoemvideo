#Crie um algoritmo que leia um número e mostre o seu dobro, trilo e a raiza quadrada.
num = float(input("Me dê um número:"))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)

print("O dobro de {} vale {}. \n"
      "O triplo de {} vale {}. \n"
      "A raiz quadrada de {} é igual a {:.2f}.".format(num, dob, num, tri, num, raiz))
