peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? ").replace(",","."))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Acima do peso")
elif imc >= 30 and imc <= 40:
    print("Obeso")
elif imc > 40:
    print("Obesidade mórbida")