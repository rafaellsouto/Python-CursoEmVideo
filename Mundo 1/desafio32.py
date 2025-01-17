# import calendar
#
# ano = int(input('Qual o ano: '))
# bissexto = calendar.isleap(ano)
#
# if bissexto:
#     print('{} é ano bissexto'.format(ano))
# else:
#     print('{} não é ano bissexto'.format(ano))

ano = int(input('Qual o ano: '))

if ( ano % 4 == 0 ) and ( ano % 100 != 0 ):
    print('{} é ano bissexto'.format(ano))
else:
    print('{} não é ano bissexto'.format(ano))