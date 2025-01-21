numero = 0
total = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        soma = soma + numero
        total += 1

print(f'Ao todo foram digitados {total} e a soma é {soma}')