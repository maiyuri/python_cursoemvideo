lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita')
#tuplas são imutáveis
#lance(1) = 'coxinha' <--- nao funciona, pq tupla é imutável

for c in range(0, len(lanche)):
   print(f'Eu vou comer {lanche[c]}')

for c in lanche:
   print(f'Eu vou comer {c}')
print('Obrigada!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {pos}:{comida}.')
print('Comi pra caramba!')
