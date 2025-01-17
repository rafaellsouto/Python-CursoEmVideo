numero = int(input('Numero: '))

contador = 0

print('='*12)
while contador <= 10:
    print('{} x {} = {}'.format(numero, contador, numero * contador))
    contador += 1
print('='*12)