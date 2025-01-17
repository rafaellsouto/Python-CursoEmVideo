from random import randint

numeroUsuario = 0
numeroPC = randint(1,10)
opção = ''
soma = 0
vitorias = 0

print('=-'*7)
print('PAR OU IMPAR')
print('=-'*7)
while True:
    numeroUsuario = int(input('Digite um valor: '))
    opção = str(input('Par ou ímpar? [P/I]: ')).upper()
    soma = numeroPC + numeroUsuario

    # se a soma der par e ele tiver jogado par
    if soma % 2 == 0:
        print(f'O PC jogou {numeroPC} e você jogou {numeroUsuario} e a soma é {soma} deu PAR.')

        print('=-' * 7)
        if opção == 'P':
            print('VOCÊ GANHOU!')
            vitorias+=1
        else:
            print('VOCÊ PERDEU!')
            print('=-' * 7)
            break
        print('=-' * 7)
    else: # se soma der impar e ele tiver jogado impar
        print('=-' * 20)
        print(f'O PC jogou {numeroPC} e você jogou {numeroUsuario} e a soma é {soma} deu ÍMPAR.')

        print('=-' * 7)
        if opção == 'P':
            print('VOCÊ PERDEU!')
            print('=-' * 7)
            break
        else:
            print('VOCÊ GANHOU!')
            vitorias += 1
        print('=-' * 7)

print(f'GAME OVER! Você ganhou {vitorias} vezes')
