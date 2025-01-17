nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = ( nota1 + nota2 ) / 2

print(media)
if media <= 5.0:
    print('\033[0:31mREPROVADO\033[0:32m')
elif media > 5.0 and media < 6.9:
    print('\033[0:36mRECUPERAÇÃO\033[0:32m')
else:
    print('\033[0:32mAPROVADO\033[0:32m')
