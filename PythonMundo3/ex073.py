print(60*'*')
print('     CAMPEONATO BRASILEIRO DE FUTEBOL - SÉRIE A - 2021')
print(60*'*')

tabela = ('Red Bull Bragantino - SP', 'Athletico Paranaense - PR', 'Fortaleza - CE',
          'Palmeiras - SP', 'Atlético - GO', 'Atlético Mineiro - MG', 'Flamengo - RJ',
          'Fluminense - RJ', 'Bahia - BA', 'Santos - SP', 'Corinthians - SP', 'Ceará - CE',
          'Internacional - RS', 'Juventude - RS', 'Sport - PE', 'Cuiabá - MT', 'São Paulo - SP',
          'Chapecoense - SC', 'America - MG', 'Grêmio - RS')

while True:
    menu = int(input('''O que você deseja visualizar?
    [1] Apenas os 5 primeiros colocados.
    [2] Os últimos 4 colocados.
    [3] Uma lista com o Top 20 de nome dos times em ordem alfabética.
    [4] Saber em que posição da tabela está o time da Chapecoense.
    [5] Sair do programa.
    Sua opção: '''))
    if menu == 1:
        print(60 * '*')
        for i in range(0, 5):
            print(f"TOP {i + 1}: {tabela[i]} ")
        print(60 * '*')
    if menu == 2:
        print(60 * '*')
        for i in range(4, 0, -1):
            print(f'{tabela[-i]}')
        print(60 * '*')
    if menu == 3:
        print(60 * '*')
        print(sorted(tabela), end= "\n")
        print(60 * '*')
    if menu == 4:
        print(60 * '*')
        for pos, time in enumerate(tabela):
            if time == 'Chapecoense - SC':
                print(f"O time {time} esta na {1 + pos}º posição.")
        print(60 * '*')
    if menu == 5:
        break

print("Programa finalizado, volte sempre!")

