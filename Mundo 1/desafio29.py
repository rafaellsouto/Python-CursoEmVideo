velocidadeMedida = int(input('Qual a velocidade medida: '))

if velocidadeMedida > 80:
    print('Excedeu o limite.','\n', 'Multa: {}'.format((velocidadeMedida - 80) * 7))
