pessoas = list()
pessoa = dict()
op = ''
total = 0
soma = 0
média = 0.0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    pessoas.append(pessoa.copy())
    total = total + 1
    while True:
        op = str(input('Continuar adicionando pessoas [s/n]? ')).upper()[0]
        if op != 'SN':
            break
        print('Erro! Por favor, digite apenas s ou n')
    if op == 'N':
        break

média = soma / total

print(f'- O grupo tem {total} pessoas.')
print(f'- A média de idade foi {média:2}')
print('- As mulheres cadastradas foram: ', end=' ')
for i in range(total):
    if pessoas[i]['sexo'] == 'F':
        print(f'{pessoas[i]["nome"]}', end=' ')
print()
print('- Lista de pessoas que estão acima da média de idade: ')
for i in range(total):
    if pessoas[i]['idade'] > média:
        print(f'nome = {pessoas[i]["nome"]}; sexo = {pessoas[i]["sexo"]}; idade = {pessoas[i]["idade"]}')
