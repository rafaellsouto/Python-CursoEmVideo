# desafio 28
import random

numeroPC = int(random.randint(1,10))

numeroUsuario = int(input('Digite um número: '))

print('Adivinhou' if numeroPC == numeroUsuario else 'Errou')
print(numeroPC)