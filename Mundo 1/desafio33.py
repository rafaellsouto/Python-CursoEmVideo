one = int(input('Digite o primeiro numero: '))
two = int(input('Digite o segundo numero: '))
three = int(input('Digite o terceiro numero: '))

maior = one
menor = 0

if maior < two and two > three:
    maior = two
elif maior < three and three > two:
    maior = three
if menor > two and two < three:
    menor = two
elif menor > three and three < two:
    menor = three
else:
    menor = one

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))