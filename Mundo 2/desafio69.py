idade = 0
sexo =''
opção = ''
deMaior = 0
homens = 0
menorVinte = 0

while True:
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo [M/F]: '))
    opção = str(input('Deseja continuar? [S/N]'))

    # Verifica se a opção foi s ou n
    while opção.upper() != 'S' and opção.upper() != 'N':
        print('Opção inválida.')
        opção = str(input('Deseja continuar? [S/N]'))

    # Verifica quantas pessoas são maiores de idade
    if idade >= 18:
        deMaior += 1

    # Verifica quantos homens há
    if sexo in 'mM':
        homens += 1

    # Verifica quantas mulheres menores de 20 anos há
    if sexo in 'Ff':
        if idade < 20:
            menorVinte += 1

    # Flag de parada
    if opção in 'nN': break

print('- ' * 12)
print('Fim do cadastro.')
print('- ' * 12)
print(f'Há {deMaior} maiores de idade.')
print(f'Foram cadastrado {homens} homens.')
print(f'Há {menorVinte} mulheres com menos de 20 anos.')