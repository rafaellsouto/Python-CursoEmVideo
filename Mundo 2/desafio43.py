peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / (altura * altura)

print('{:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')