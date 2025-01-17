from datetime import date

deMaior = 0
deMenor = 0
anoAtual = date.today().year
for r in range(1, 7):
    ano = int(input('Ano nascimento: '))
    idade = anoAtual - ano
    if idade >= 21:
        deMaior = deMaior + 1
    else:
        deMenor = deMenor + 1
print('{} são maiores de idade e {} são menores de idade.'.format(deMaior, deMenor))