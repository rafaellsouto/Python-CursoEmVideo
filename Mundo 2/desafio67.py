produto = 0

while True:
    print('-'*20)
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0: break
    count = 0
    while True:
        produto = n * count
        print(f'{n} x {count} = {produto}')
        count += 1
        if count == 11: break;
print('Programa tabuada encerrado.')