print('\033[0;33m-=-' * 8)
print('\033[1:34mAnalisador de Trinagulo\033[m')
print('\033[0;33m-=-\033[m' * 8)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Segmentos acimor PODEM FORMAR triangulo')
else:
    print('Segmentos acimor NÃO PODEM FORMAR triangulo')