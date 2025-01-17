kmRodado = float(input('Quantos km você rodou: '))
diasAlugado = int(input('Por quantos dias foi alugado: '))

preco = (kmRodado * 0.15) + (diasAlugado * 60)

print('km rodado: {}\nDias alugados: {}\nPreço: {}'.format(kmRodado, diasAlugado, preco))