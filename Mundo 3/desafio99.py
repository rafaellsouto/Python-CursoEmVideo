from time import sleep

def analise(*num):
    print('-' * 30)
    print('Valores passados: ')
    for v in num:
        print(f'{v} ', end='')
        sleep(0.5)
    print()

    print(f'Foram informados {len(num)} valores.')
    maior = num[0]
    for valor in num:
        if valor > maior:
            maior = valor
    print(f'O maior valor foi {maior}')
    sleep(2)


analise(4, 5, 6)
analise(4, 12, 5, 35, 6)
analise(14, 5, 60, 27)
analise(1, 7)
