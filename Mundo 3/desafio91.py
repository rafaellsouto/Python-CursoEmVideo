import random
from time import sleep

numSorteado = 0
jogador = dict()
jogadores = list()
aux = list()

print('Valores sorteados: ')
for i in range(1,5):
    numSorteado = random.randint(1,6)
    print(f'Jogador{i} tirou {numSorteado} ')
    sleep(1)
    jogador['nome'] = f'jogador{i}'
    jogador['num'] = numSorteado
    jogadores.append(jogador.copy())
print('Ranking dos jogadores: ')
print(jogadores)
for i in range(0,4):
    for j in range(0,4):
        if jogadores[i]['num'] < jogadores[j]['num']:
            aux.append(jogadores[i])
            jogadores.append(jogadores[j])
            jogadores.append(aux)
    print(f'{i+1}º lugar: {jogadores[i]["nome"]} com {jogadores[i]["num"]}')
    sleep(1)
