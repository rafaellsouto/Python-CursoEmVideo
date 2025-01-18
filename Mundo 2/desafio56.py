media = 0
soma = 0
qntdAteVinte = 0
nomeMaisVelho = ''
idadeMaisVelho = 0

for r in range(1,5):
    print('-' * 5, '{}ª pessoa'.format(r), '-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    # soma as idade para tirar a média
    soma += idade

    # Encontra quem é o homem mais velho e sua idade
    if idade > idadeMaisVelho and sexo == 'M':
            idadeMaisVelho = idade
            nomeMaisVelho = nome


    # Verifica quantas mulheres menores de 20 anos há
    if idade < 20 and sexo == 'F':
        qntdAteVinte += 1

media = soma / 4
print(f'A média das idades é {media}')
print(f'O homem mais velho tem {idadeMaisVelho} e se chama {nomeMaisVelho}')
print(f'Ao todo há {qntdAteVinte} mulheres menores de 20 anos.')