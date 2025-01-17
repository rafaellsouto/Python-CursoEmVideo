distViagem = int(input('Qual a distancia do trajeto da sua viagem: '))

if distViagem > 200:
    valor = distViagem * 0.45
    print('Valor: {}'.format(valor))
else:
    valor = distViagem * 0.5
    print('Valor: {}'.format(valor))