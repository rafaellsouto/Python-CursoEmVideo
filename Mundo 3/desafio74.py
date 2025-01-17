import random
lista = [1, 2 , 3 ,4, 5]
numeros = ( lista )
# numero = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for i in range(0, 5):
    lista[i] = random.randint(1, 100)

print(f'Os números gerados foram {numeros}')

for r in range(0, 5):
    if r == 0:
        maior = menor = numeros[0]
    if maior < numeros[r]:
        maior = numeros[r]
    elif menor > numeros[r]:
        menor = numeros[r]

print(f'O maior valor é {maior}, e o menor é {menor}')
print(f'O maior valor é {max(numeros)}, e o menor é {min(numeros)}')
