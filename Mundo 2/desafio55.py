peso = 0
maior = 0
menor = 0

for r in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(r)))
    # Dessa forma há um bug para um sequencia ordenada de forma crescente
    # if peso > maior:
    #     maior = peso
    #     menor = maior
    #     print('maior = {}'.format(maior))
    #
    # if peso < menor:
    #     menor = peso
    #     print('menor = {}'.format(menor))

    if r == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O mais pesado tem {maior} KG')
print(f'O mais leve tem {menor} KG')