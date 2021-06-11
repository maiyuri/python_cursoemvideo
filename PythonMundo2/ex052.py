num = int(input("Me diga um número: "))
mult = 0
qtdmult = 0
for c in range(1, num+1):
    if num % c == 0:
        print("Esse número é multiplo de {}".format(c))
        mult += 1
if mult == 2:
    print("É primo")
else:
    print("Esse número tem {} mútiplos, nao e primo".format(mult))
