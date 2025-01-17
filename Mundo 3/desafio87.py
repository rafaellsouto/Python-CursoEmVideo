matriz = []
temp = []
soma_pares = somaTercCol = maiorSegunLinha = 0
for m in range(0, 3):
    for n in range(0, 3):
        temp.append(int(input(f'Valor para a posição [{m}][{n}]: ')))
    matriz.append(temp[:])
    temp.clear()
for l in range(0, 3):
    maiorSegunLinha = matriz[1][0]
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            somaTercCol += matriz[l][2]
        if matriz[1][c] > maiorSegunLinha:
            maiorSegunLinha = matriz[1][c]
    print()
print(f'A soma dos pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {somaTercCol}')
print(f'O maior valor da segunda linha é {maiorSegunLinha}')