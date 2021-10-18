linha = ('Chocolate', 1.75, 'Leite', 3.50, 'Frango', 10.90)
#linha = [1, 100000.00, 9282.21, 8333.33, 948.88, 91666.67

print("-"*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-"*40)


for i in range(0, len(linha)):
    if i % 2 == 0:
        print(f'{linha[i]:.<30}', end='')
    else:
        print(f'R${linha[i]:>5.2f}')
print("-"*40)