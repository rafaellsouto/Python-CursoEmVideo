from time import sleep

def analise(*num):
    if num == None:
        maior = 0
        tam = 0
    print('-' * 30)
    tam = len(num)
    print('Valores passados: ')
    for v in num:
        print(f'{v} ', end='')
        sleep(0.5)
    print()

    print(f'Foram informados {tam} valores.')
    maior = 0 # num[0]
    for valor in num:
        if valor > maior:
            maior = valor
    print(f'O maior valor foi {maior}')
    sleep(2)


analise(4, 5, 6)
analise(4, 12, 5, 35, 6)
analise(14, 5, 60, 27)
analise(1, 7)
analise()
