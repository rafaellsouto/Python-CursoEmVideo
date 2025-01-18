numero = int(input('Digite um número: '))
divs = 0

for r in range(1, numero + 1):
    if numero % r == 0:
        print('\033[33m', end=' ')
        divs = divs + 1
    else:
        print('\033[34m', end=' ')
    print(f'{r}', end=' ')
    print('\033[m', end=' ')
if divs == 2:
    print(f'\n{numero} é primo.')
else:
    print(f'\n{numero} não é primo, pois é divisível por {divs} números')