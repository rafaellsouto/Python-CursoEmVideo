valorCasa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual seu salario?: '))
anosPagamento = int(input('Período de financiamento: '))
limitePrestacao = salario * 0.3
valorPrestacao = (valorCasa / anosPagamento) / 12

if valorPrestacao > limitePrestacao:
    print('Negado')
else:
    print('Financiamento concedido\nVocê pagará {} / mês durante {} anos.'.format(valorPrestacao, anosPagamento))