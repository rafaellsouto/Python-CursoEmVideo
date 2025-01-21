primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
count = primeiro
qntdTermos = 1


while qntdTermos != 0:
    while count <= decimo:
        print(count)
        count += razao

        if count > decimo:
            qntdTermos = int(input('Deseja ver mais quantos termos: '))

            if qntdTermos != 0:
                primeiro = count
                decimo = primeiro + (qntdTermos - 1) * razao

print('Programa finalizado.')