n1 = float(input("Adicione a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2
print("A sua média foi {:.1f}".format(media))
if media >= 6.0:
    print("Sua nota esta boa")
else:
    print("sua nota esta ruim!")
