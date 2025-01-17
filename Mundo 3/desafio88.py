from time import sleep
from random import randint
jogos = []
temp = []
print('-' * 12)
print('Mega Sena')
print('-' * 12)
qntdJogos = int(input('Quantos jogos vc quer que eu sorteie?: '))
print(f'-=-=-= Sorteando {qntdJogos}  jogos -=-=-=')
for j in range(0, qntdJogos):
    for i in range(0, 6):
        numero = randint(1, 60)
        if numero in temp:
            numero = randint(1, 60)
        temp.append(numero)
    jogos.append(temp[:])
    temp.clear()
for r in range(0, qntdJogos):
    print(f'Jogo {r + 1}: {sorted(jogos[r])}')
    sleep(2)
