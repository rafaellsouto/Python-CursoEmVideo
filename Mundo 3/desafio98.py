from time import sleep

def contador():
    print('CONTAGEM DE 1 ATÉ 10:')
    for j in range(1, 11):
        print(f'{j} ', end='')
        sleep(0.5)
    print('FIM.')
    print('=' * 30)
    print('CONTAGEM DE 10 ATÉ 0 DE 2 EM 2: ')
    for h in range(10, -1, -2):
        print(f'{h} ', end='')
        sleep(0.5)
    print('FIM.')
    print('=' * 30)
    print('Agora é a sua vez, entre com os valores para: ')
    inicio = int(input('Digite o início: '))
    fim = int(input('Digite o fim: '))
    passo = int(input('Digite o passo: '))

    if passo < 0:
        passo = abs(passo)

    if passo == 0:
        passo = 1

    print(f'CONTAGEM DE {inicio} ATÉ {fim} DE {passo} EM {passo}: ')

    if inicio > fim:
        passo = passo * -1

    for i in range(inicio, fim-1, passo):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM.')


contador()
