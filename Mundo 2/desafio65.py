numero = 0
soma = 0
media = 0.0
total = 0
maior = 0
menor = 0
opção = ''

while opção != 'N':
    numero = int(input('Digite um número: '))
    soma = soma + numero
    total += 1 # conta quantos valores foram digitados

    # Encontra maior e menor valor
    if maior == 0 and menor == 0:
        maior = numero # Inicializa maior para a primeira ocorrência
        menor = numero # Inicializa menor para a primeira ocorrência
    else:
        if numero > maior:
            maior = numero
        else:
            menor = numero

    opção = str(input('Quer continuar[S/N]: ')).upper()

    # Garante que só será digitado S ou N
    if opção != 'S' and opção != 'N':
        while opção != 'S' and opção != 'N':
            print('Opção inválida.')
            opção = str(input('Quer continuar[S/N]: ')).upper()

media = soma / total

print(f'A média é {media}\nO maior valor é {maior} e o menor é {menor}')