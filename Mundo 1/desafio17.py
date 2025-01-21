from math import sqrt
catetoOposto = int(input('Qual o valor do cateto oposto: '))
catetoAdjacente = int(input('Qual o valor do cateto adjacente: '))
hipotenusa = catetoAdjacente**2 + catetoOposto**2

print(sqrt(hipotenusa))
