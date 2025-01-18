from random import randint
count = 0
numeroPC = randint(0,10)
numeroUsuario = 0

while count != 10:
    numeroUsuario = int(input('Qual seu palpite: '))
    if numeroUsuario == numeroPC:
        print('Você acertou jogando {} vezes'.format(count+1))
        break
    else:
        if numeroUsuario > numeroPC:
            print('Você errou, tente um valor menor.')
        else:
            print('Você errou, tente um valor maior.')
        count += 1