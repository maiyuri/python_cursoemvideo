tempo = int(input("Quanto tempo tem o seu carro? "))

if tempo <= 3:
    print("Carro novo")
elif tempo == 4 or tempo == 5:
    print("nem novo nem velho, é mais ou menos")
else:
    print("Seu carro é velho!")
