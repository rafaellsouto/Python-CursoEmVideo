opção = 0

primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))

while opção != 5:
    print(' [1] Somar\n',
          '[2] Multiplicar\n',
          '[3] Maior\n',
          '[4] Novos Números\n',
          '[5] Sair do programa\n'
          )
    opção = int(input('Escolha uma opção: '))

    if opção == 1:
        print('A soma entre {} + {} = {}'.format(primeiro, segundo, primeiro + segundo))

    elif opção == 2:
        print('o produto entre {} x {} = {}'.format(primeiro, segundo, primeiro * segundo))

    elif opção == 3:
        maior = 0
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo

        print('O maior valor entre [{}] e [{}] é [{}]'.format(primeiro, segundo, maior))
        
    elif opção == 4:
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))

        print('Você digitou os números {} e {}'.format(primeiro, segundo))
    elif opção == 5:
        print('Você saiu do programa.')
    else:
        print('Opção inválida, tente novamente.')
        print()

