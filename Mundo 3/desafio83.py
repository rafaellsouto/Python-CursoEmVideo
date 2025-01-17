expressão = []
aberto = 0
fechado = 0

expressão.append(input('Digite uma expressão: '))

for i in range(0, len(expressão)): # mais adequado a sintaxe python seria for simbolo in expressão:
    if expressão[i] == '(': # no lugar de espressão[i] -> simbolo
        aberto = aberto + 1
    elif expressão[i] == ')':
        fechado = fechado + 1

if aberto == fechado:
    print('Expressão válida.')
else:
    print('Expressão não é válida.')


# # solução do Guanabara
# espressão = str(input('Digite uma expressão: '))
# pilha = list()
# for símbolo in espressão:
#     if símbolo == '(':
#         pilha.append('(')
#     elif símbolo == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Expressão válida.')
# else:
#     print('Expressão inválida.')