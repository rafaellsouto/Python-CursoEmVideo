sexo = ''
count = 1
while count == 1:
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
    if sexo == 'F' or sexo == 'M':
        count = 0
    else:
        print('Sexo inválido, digite novamente.')

print('Sexo informado corretamente.')