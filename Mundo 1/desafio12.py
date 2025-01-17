notebook = 3500
galaxyWatch5 = 1600
galaxyBuds2Pro = 614

print('1- Notebook = 3500\n2 -Galaxy Watch 5 = 1600\n3- Galaxy Buds 2 Pro')
escolha = int(input('Esolha a opção: '))

if escolha == 1:
    print('Notebook R$ {}, valor com desconto {}'.format(notebook, notebook - (notebook*5/100)))
elif escolha == 2:
    print('Galaxy Watch 5 R$ {}, valor com desconto {}'.format(galaxyWatch5, galaxyWatch5 - (galaxyWatch5 * 5 / 100)))
elif escolha == 3:
    print('Galaxy Buds 2 Pro R$ {}, valor com desconto {}'.format(galaxyBuds2Pro, galaxyBuds2Pro - (galaxyBuds2Pro * 5 / 100)))