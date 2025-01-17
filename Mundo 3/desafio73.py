atletas =('Fábio Giga',
          'Alfy Polly',
          'Caike Pro',
          'Amanda Curvelo',
          'Gabriel Arones',
          'Felipe Franco',
          'Gnomo',
          'Gorgonoid',
          'Balestrin',
          'Big Jeff',
          'Léo Stronda',
          'Ju Chitarra',
          'Roberta Zuniga',
          'Renato Cariani',
          'Eduardo Edoc',
          'Daniele Mendonça ',
          'Bruno Macedo',
          'Rafael Adão',
          'Victor Lelis',
          'Tenente Eusébio',
          'Cavalo')

print('-=' * 12)
print('Listas de atletas: ', atletas)
print('-=' * 12)
print(f'Os 5 primeiros são {atletas[:5]}')
print('-=' * 12)
print(f'Os 4 últimos são {atletas[-4:]}')
print('-=' * 12)
print(f'Em ordem alfabetica: {sorted(atletas)}')
print('-=' * 12)
print(f'Balestrin está na {atletas.index('Balestrin')}ª posição')