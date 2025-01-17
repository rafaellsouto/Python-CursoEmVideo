nome = ''
preço = 0.0
total = 0.0
maisDeMil = 0
maisBarato = 0.0
nomeMaisBarato = ''

print('=' * 12)
print('LOJA STAND BY')
print('=' * 12)

while True:
    nome = str(input('Qual o nome do produto: '))
    preço = float(input('Qual o preço do produto: '))
    opção = str(input('Deseja continuar? [S/N]'))

    # Verifica se a opção foi s ou n
    while opção.upper() != 'S' and opção.upper() != 'N':
        print('Opção inválida.')
        opção = str(input('Deseja continuar? [S/N]'))

    # soma o valor total
    total += preço

    # Verifica quantos são mais de R$ 1000
    if preço > 1000:
        maisDeMil += 1

    # Verifica qual o produto mais barato
    if maisBarato == 0:
        maisBarato = total
    elif maisBarato > preço:
        maisBarato = preço
        nomeMaisBarato = nome

    # Flag de parada
    if opção in 'nN': break

print('_' * 20)
print(f'O total foi {total}.')
print(f'Tem {maisDeMil} que custam mais de R$ 1000.')
print(f'O produto mais barato é o(a) {nomeMaisBarato} que custa R$ {maisBarato}.')