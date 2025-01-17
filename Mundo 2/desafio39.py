from datetime import date

yearWasBorn = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - yearWasBorn

if idade == 18:
    print('Está na hora de alistar-se')
elif idade < 18:
    print('Ainda falta {} para você alistar-se'.format(18 - idade))
    anoAlistamento = (18 - idade) + date.today().year
    print('Seu alistamento será em {}'.format(anoAlistamento))
else:
    print('Já passou a idade de alistar-se')
    anoAlistamento = date.today().year - (idade - 18)
    print('Seu alistamento foi em {}'.format(anoAlistamento))