# matriz = []
# primeira_linha = []
# segunda_linha = []
# terceira_linha = []
# for l in range(0, 3):
#     primeira_linha.append(int(input('Digite o valor para a posição')))
# matriz.append(primeira_linha[:])
# for l in range(0, 3):
#     segunda_linha.append(int(input('Digite o valor para a posição')))
# matriz.append(segunda_linha[:])
# for l in range(0, 3):
#     terceira_linha.append(int(input('Digite o valor para a posição')))
# matriz.append(terceira_linha[:])
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]}]', end=' ')
#     print()

# lista = []
# outra_lista = []
# lista.append(10)
# lista.append(20)
# outra_lista.append(lista[:])
# outra_lista[0].append(30)
# mais_uma_lista = []
# mais_uma_lista.append(40)
# mais_uma_lista.append(50)
# outra_lista.insert(0, mais_uma_lista[:])
# outra_lista.insert(outra_lista[1][0], 60)
# print(outra_lista)

matriz = []
temp = []
for m in range(0, 3):
    for n in range(0, 3):
        temp.append(int(input(f'Valor para a posição [{m}][{n}]: ')))
    matriz.append(temp[:])
    temp.clear()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
