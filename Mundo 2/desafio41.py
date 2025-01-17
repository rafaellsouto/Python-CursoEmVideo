from datetime import date

categorias = ['mirim', 'infantil', 'junior', 'senior', 'master']
anoNasc = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - anoNasc

if idade <= 9:
    print(categorias[0])
elif idade <= 14:
    print(categorias[1])
elif idade <= 19:
    print(categorias[2])
elif idade <= 20:
    print(categorias[3])
else:
    print(categorias[4])