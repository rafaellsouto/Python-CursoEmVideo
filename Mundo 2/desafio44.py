print('{:=^15}'.format('Produtos'))
print('-' * 10)
print(  '1 - galaxy watch - R$ 1200.0\n',
        '2 - galaxy buds 2 pro - R$ 750.00')
opcaoProduto = int(input())

print('=' * 20)
print('Método de pagamento')
print('=' * 20)
print('1 - à vista 10% OFF')
print('2 - à vista no cartão 5% OFF')
print('3 - 2x no cartão')
print('4 - 3x ou mais com 20% de juros')
print('=' * 20)
opcaoPagamento = int(input())

if opcaoProduto == 1 and opcaoPagamento == 1:
    print('O valor a ser pago será {}'.format( 1200 - (1200 * 0.1) ))
elif opcaoProduto == 1 and opcaoPagamento == 2:
    print('O valor a ser pago será {}'.format( 1200 - (1200 * 0.05) ))
elif opcaoProduto == 1 and opcaoPagamento == 3:
    print('O valor a ser pago será {}/ parcela'.format( 1200 / 2 ))
elif opcaoProduto == 1 and opcaoPagamento == 4: # fim do produto 1
    parcelas = int(input('Quantas parcelas: '))
    print('O valor a ser pago será {}/ parcela'.format( (1200 + (1200 * 0.2)) / parcelas ))
if opcaoProduto == 2 and opcaoPagamento == 1:
    print('O valor a ser pago será {}'.format( 750 - (750 * 0.1) ))
elif opcaoProduto == 2 and opcaoPagamento == 2:
    print('O valor a ser pago será {}'.format( 750 - (750 * 0.05) ))
elif opcaoProduto == 2 and opcaoPagamento == 3:
    print('O valor a ser pago será {}/ parcela'.format( 750 / 2 ))
elif opcaoProduto == 2 and opcaoPagamento == 4:
    parcelas = int(input('Quantas parcelas: '))
    print('O valor a ser pago será {}/ parcela'.format( (750 + (750 * 0.2)) / parcelas ))