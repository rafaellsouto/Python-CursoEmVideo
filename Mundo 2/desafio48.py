soma = 0
for r in range(1, 500):
    if r % 3 == 0 and r % 2 != 0:
        soma = soma + r
print(soma)