boletim = list()
temp = []
notas = []
média = 0
while True:
    nome = str(input('Nome do aluno: '))
    temp.append(nome)
    nota1 = float(input('Primeira nota: '))
    notas.append(nota1)
    nota2 = float(input('Segunda nota: '))
    notas.append(nota2)
    temp.append(notas[:])
    média = ( nota1 + nota2 ) / 2
    temp.append(média)
    boletim.append(temp[:])
    temp.clear()
    notas.clear()
    opção = str(input('Deseja adicionar mais alunos?[S/N]: '))
    if opção in 'Nn':
        break
print('='*12)
print('ID  NOME      MÉDIA')
for i in range(0, len(boletim)):
    print(f'{i}  {boletim[i][0]}       {boletim[i][2]}')
print('='*12)
while True:
    aluno = int(input('Mostrar as notas de qual aluno? [999 - interromper]: '))
    if aluno == 999:
        break
    print(f'Notas de {boletim[aluno][0]} são {boletim[aluno][1]}') #  e {boletim[aluno][2]}
