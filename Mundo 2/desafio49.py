numero = int(input('Digite um número para ver sua tabuada: '))

for r in range(1, 11):
    print('{} x {} = {}'.format(numero, r, numero * r))