from random import randint
from time import sleep

# print('=' * 20)
# print('       Jokenpô')
# print('=' * 20)
# print('1 - pedra\n2 - papel\n3 - tesoura')
# print('-' * 20)
#
# opcao = int(input('Escolha uma opção: '))
#
# if numero == opcao:
#     print('Empate')
# elif numero == 1 and opcao == 2:
#     print('Usuário ganhou')
# elif numero == 1 and opcao == 3:
#     print('PC ganhou')
# elif numero == 2 and opcao == 1:
#     print('PC ganhou')
# elif numero == 2 and opcao == 3:
#     print('Usuário ganhou')
# elif numero == 3 and opcao == 1:
#     print('Usuário ganhou')
# elif numero == 3 and opcao == 2:
#     print('PC ganhou')
#
# print('PC jogou {}'.format(numero))

#######################################
itens = ('Pedra', 'Papel', 'Tesoura')
numero = randint(1,3)

print('''Suas opções: 
      [1] Pedra
      [2] Papel
      [3] Tesoura''')

jogador = int(input('Escolha uma opção: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

if numero == jogador:
     print('Empate')
elif numero == 1 and jogador == 2:
     print('Usuário ganhou')
elif numero == 1 and jogador == 3:
     print('PC ganhou')
elif numero == 2 and jogador == 1:
     print('PC ganhou')
elif numero == 2 and jogador == 3:
     print('Usuário ganhou')
elif numero == 3 and jogador == 1:
     print('Usuário ganhou')
elif numero == 3 and jogador == 2:
     print('PC ganhou')

print('O pc jogou {} e vc jogou {}'.format(itens[numero - 1], itens[jogador - 1]))
