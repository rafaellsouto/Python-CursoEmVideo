numExtenso = ('zero',
              'um',
              'dois',
              'três',
              'quatro',
              'cinco',
              'seis',
              'sete',
              'oito',
              'nove',
              'dez',
              'onze',
              'doze',
              'treze',
              'quatorze',
              'quinze',
              'dezesseis',
              'dezessete',
              'dezoito',
              'dezenove',
              'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >= 0 and numero <= 20:
        break
    print('Número não é válido. Tente novamente.')
print(f'Você digitou o número {numExtenso[numero]}')


# supps = ('Creatina', 'Whey', 'Ômega 3', 'Multivitaminico')
#
# print(supps[0:3])
# print(supps[2:])
# print(supps[:3])
# print(supps[-3])
#
# for supp in supps:
#     print(f'Eu vou usar {supp}')
#
# for pos, supp in enumerate(supps):
#     print(f'Eu vou usar {supp} - {pos}')
#
# print(sorted(supps))
#
# a = (1, 3, 5)
# b = (2, 4, 6)
# print(a)
# print(b)
# c = a + b
# print(c)
# c = b + a
# print(c)
#
# # métodos da tupla count, index
#
# print(a.index(5))