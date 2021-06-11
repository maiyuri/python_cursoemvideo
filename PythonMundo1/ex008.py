#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

num = float(input("Me dê um valor em metros: "))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cen = num * 100
mil = num * 1000

print("Esse valor em\n"
      "kilometro é {} em\n"
      "Hectometros é {} e em\n"
      "Decametros é {} em \n"
      "Metro é {} \n"
      "decimetros é {} em\n"
      "centimetros é {} e\n"
      "milimetros é {}\n".format(km, hm, dam, num, dm, cen, mil))
