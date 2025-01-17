jogador = dict()
gols = list()
total = 0

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}?: ')))
    total = total + gols[i]
jogador['gols'] = gols
jogador['total'] = total
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(jogador)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(partidas):
    print(f'\t=> Na partida {i+1}, fez {jogador["gols"][i]} gols')
print(f'Foi um total de {jogador["total"]} gols.')