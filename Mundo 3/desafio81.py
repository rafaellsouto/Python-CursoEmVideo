numeros = []
totNum = 0
while True:
    valor = int(input('Informe um valor: '))
    numeros.append(valor)
    totNum += 1
    op = input('Deseja continuar? [S/N]: ').upper()
    if op != 'S':
        break
print('|=' * 15)
print(f'Foram digitados {totNum} numeros.')
print(f'A lista ordenada é decrescente {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O número \033[32m5\033[m está presente na lista.')
else:
    print('O número \033[31m5\033[m não está presente na lista.')
