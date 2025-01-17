jogador = dict()
gols = list()
time = list()
total = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}?: ')))
        total = sum(gols)
    jogador['gols'] = gols[:]
    jogador['total'] = total
    time.append(jogador.copy())
    while True:
        op = str(input('Deseja continuar? [s/n] ')).upper()[0]
        if op in 'SN':
            break
        print('Erro. Digite apenas S ou N.')
    if op == 'N':
            break
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:<9}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<10}',end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro. Não existe jogador com código ', busca)
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'\tNo jogo {i+1} fez {g} gols.')
    print('-' * 40)
print(' << VOLTE SEMPRE >>')