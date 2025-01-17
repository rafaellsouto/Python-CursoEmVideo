numeros = []
pares = []
impares = []

numeros = []
while True:
    numeros.append(int(input('Informe um valor: ')))
    op = input('Deseja continuar? [S/N]: ').upper()
    if op != 'S':
        break
print('|=' * 15)
for pos, valor in enumerate(numeros):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'Os números digitados foram {numeros}')
print(f'Os números pares são {pares}')
print(f'Os números impares são {impares}')