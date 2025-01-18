primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
count = primeiro

while count <= decimo:
    print(count)
    count += razao