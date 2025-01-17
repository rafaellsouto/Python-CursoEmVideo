# valores = []
# aux = 0
#
# for p in range(0, 5):
#     valor = int(input('Digite um valor: '))
#     valores.append(valor)
# for v in range(0, 5):
#     for p in range(v, 5):
#         if valores[v] > valores[p]:
#             aux = valores[v]
#             valores[v] = valores[p]
#             valores[p] = aux
# print(valores)

# # Resolução do Guanabara
lista = list()

for p in range(0, 5):
    n = int(input('Digite um valor: '))
    if p == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao fim da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(lista)