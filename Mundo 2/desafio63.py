# x termos da sequencia de fibonacci

numero = int(input('Digite a quantidade de termos: '))
ultimo = 0
penultimo = 1
count = 0

while count < numero:

    if count == 0:
        print(0)

    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print(termo)
    count += 1