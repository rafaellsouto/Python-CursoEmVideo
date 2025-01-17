lista = [0,0,0,0]
valores = ( lista )
for i in range(0, 4):
    lista[i] = int(input('Digite um valor: '))

print(f'Os valores digitados foram {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O número 3 está na {valores.index(3)+1}ª posição.')
else:
    print('O número 3 não está presente na tupla.')

print(f'Os números pares foram ', end='')
for i in range(0, 4):
    if valores[i] % 2 == 0:
        print(valores[i], end=' ')