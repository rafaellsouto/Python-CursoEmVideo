print('Conversor de bases númericas')
num = int(input('Digite um número para conversão: '))
print('[1] Binário\n[2] Octadecimal\n[3] Hexadecimal')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} em binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} em octadecimal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')

