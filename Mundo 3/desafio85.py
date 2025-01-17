números = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)
números[0].sort()
números[1].sort()
print(f'Os números pares são: {números[0]}')
print(f'Os números impares são: {números[1]}')