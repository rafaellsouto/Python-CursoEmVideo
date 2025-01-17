alunos = dict()

alunos['Nome'] = str(input('Nome do aluno: '))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'
# print(f'{alunos["Nome"]} foi {alunos["Situação"]} com a média {alunos["Média"]}')
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
