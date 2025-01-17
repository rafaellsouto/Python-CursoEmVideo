from datetime import date
anoAtual = date.today().year
dadosFunc = dict()
nome = str(input('Nome: '))
dadosFunc['Nome'] = nome
anoNasc = int(input('Ano de nascimento: '))
dadosFunc['Idade'] = (anoAtual - anoNasc)
carteira = int(input('Carteira de Trabalho [0 se não tiver]: '))
dadosFunc['Carteira'] = carteira
if dadosFunc['Carteira'] != 0:
    dadosFunc['Admissão'] = int(input('Ano de admissão: '))
    dadosFunc['Sálario'] = float(input('Sálario: '))
    dadosFunc['Aposentadoria'] = (dadosFunc['Idade'] + 35) - (anoAtual - dadosFunc['Admissão'])

print(dadosFunc)
for k, v in dadosFunc.items():
    print(f'O {k} é {v}')

