print('=' * 12)
print('BANCO RLS')
print('=' * 12)

valor = int(input('Quanto deseja sacar? R$ '))

resto = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

nota50 = valor // 50
resto = valor - (nota50 * 50)
print(f'Total de {nota50} Cédulas de R$ 50')

nota20 = resto // 20
resto = resto - (nota20 * 20)
print(f'Total de {nota20} Cédulas de R$ 20')

nota10 = resto // 10
resto = resto - (nota10 * 10)
print(f'Total de {nota10} Cédulas de R$ 10')

nota1 = resto
print(f'Total de {nota1} Cédulas de R$ 1')

print('O banco RLS agradece a preferencia. Volte sempre.')
