frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
inverso = junto[::-1] # começa no inicio, termina no fim, mas na ordem inversa
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')