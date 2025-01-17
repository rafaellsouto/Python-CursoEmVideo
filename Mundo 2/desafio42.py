print('\033[0;33m-=-' * 8)
print('\033[1:34mAnalisador de Trinagulo\033[m')
print('\033[0;33m-=-\033[m' * 8)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('\033[0:36mEquilatero\033[m')
    elif r1 != r2 != r3:
        print('\033[0:32mEscaleno\033[m')
    else: #elif r3 != r1 and r1 == r2 or r3 == r1 and r1 != r2 or r2 == r3 and r1 != r2:
        print('\033[0:33mIsosceles\033[m')
else:
    print('\033[0:31mSegmentos acimor NÃO PODEM FORMAR triangulo\033[m')
