soma = 0
for r in range(1,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = soma + numero
print('A soma dos pares é {}'.format(soma))