from random import randint
from time import sleep

def sorteia(numeros):
    valor = 0
    print('Números sorteados: ')
    for i in range(1, 6):
        valor = randint(1, 10)
        print(f'{valor} ', end='')
        sleep(0.5)
        numeros.append(valor)



def somaPar(numeros):
    soma = 0
    for r, num in enumerate(numeros):
        if num % 2 == 0:
            soma = soma + num
    print(f'\nA soma dos valores pares da lista é {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

