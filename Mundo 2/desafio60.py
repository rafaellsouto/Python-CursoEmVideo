numero = int(input('Digite um número para calcular o fatorial: '))
count = 1
fatorial = 1

while count <= numero:
    fatorial *= count
    count += 1
print('O fatorial de {} é {}'.format(numero, fatorial))