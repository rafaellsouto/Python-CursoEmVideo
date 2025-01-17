numeros = []
while True:
    valor = int(input('Informe um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado não será adicionado.')
    op = input('Deseja continuar? [S/N]: ').upper()
    if op == 'N':
        break
print('-=' * 20)
print(f'Você digitou os valores {sorted(numeros)}')
