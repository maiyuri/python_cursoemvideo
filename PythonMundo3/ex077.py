#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
import re
def vogais(string):
    return re.sub('[^aeiouAEIOU]', '', string)

palavras = ('aprender', 'programar', 'linguagem'
            'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for i in palavras:
    vogais_palavras = vogais(i)
    print("Na palavra",i.upper(),"temos", vogais_palavras)
