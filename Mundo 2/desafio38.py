num1 = int(input('Primeiro valor: '))
num2 = int(input('Segungo valor: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2, num1))
else:
    print('Os valores são iguais')