#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input("Insira um número: "))
ant = num - 1
suc = num + 1
print("O número é {} o seu antecessor é {} e o sucessor é {} ".format(num, ant, suc))
