val = [] # [5, 4, 9, 1, 4, 6, 8]
maior = 0
menor = 0

for pos in range(0, 5):
    val.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if pos == 0:
        maior = val[0]
        menor = maior
    else:
        if maior < val[pos]:
            maior = val[pos]
        elif menor > val[pos]:
            menor = val[pos]
print(f'Lista digitada: {val}')
print(f'O maior valor é {maior} na posição', end=' ')
for i, v in enumerate(val):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor é {menor} na posição', end=' ')
for i, v in enumerate(val):
    if v == menor:
        print(f'{i}... ', end='')



# numeros = [1, 2, 4, 8]
# numeros[2] = 3
# numeros.append(6)
# numeros.insert(3, 0)
# print(numeros)
# numeros.sort(reverse=True)
# print(numeros, " = ", len(numeros))
# numeros.pop()
# numeros.append(1)
# print(numeros)
# numeros.remove(1)
# print(numeros)
#
# for pos, val in enumerate(numeros):
#     print(f'Na posição {pos} encontrei o valor {val}')
# print('Cheguei ao final da lista.')