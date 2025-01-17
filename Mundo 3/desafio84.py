# pessoas = [['Rafael', 70], ['Lucas', 60], ['Maria', 60], ['jose', 100]]

pessoas = list()
pessoa = list()
totPessoas = 0
maiorPeso = 0.0
menorPeso = 0.0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    totPessoas += 1
    pessoas.append(pessoa[:])
    pessoa.clear()
    opção = str(input('Deseja continuar: [S/N]: '))
    if opção in 'Nn':
        break
print('|=' * 14)
print(f'Foram cadastradas {totPessoas} pessoas.')
for i, p in enumerate(pessoas):
    if i == 0:
        maiorPeso = p[1]
        menorPeso = maiorPeso
    if p[1] >= maiorPeso:
        maiorPeso = p[1]
    elif p[1] < menorPeso:
        menorPeso = p[1]

print(f'O maior peso foi {maiorPeso}kg de', end=' ')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi {menorPeso}kg de', end=' ')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'{p[0]}', end=' ')


# funcionario = list()
# funcionario.append('Rafael')
# funcionario.append(21)
# escritorio = list()
# escritorio.append(funcionario[:])
# funcionario[0] = 'Lucas'
# funcionario[1] = 17
# escritorio.append(funcionario[:])
# print(escritorio)
#
# print(escritorio[0][0])
#
# for dado in escritorio:
#     print(dado)
# for nome in escritorio:
#     print(nome[0])
# for idade in escritorio:
#     print(idade[1])
#
# dado = list()
# info = list()
# for c in range(0, 2):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     info.append(dado[:])
#     dado.clear()
# print(dado)
# print(info)