import matplotlib.pyplot as plt

# Dados do relatório
idade_labels = ['Menos de 18 anos', '18 a 60 anos', 'Mais de 60 anos']
idade_values = [15, 55, 30]

genero_labels = ['Masculino', 'Feminino']
genero_values = [48, 52]

renda_labels = ['< 2 salários mínimos', '2-5 salários mínimos', '> 5 salários mínimos']
renda_values = [48, 30, 22]

ocupacao_labels = ['Emprego Formal', 'Setor Informal', 'Estudante', 'Desempregado', 'Aposen./Pens.']
ocupacao_values = [41, 23, 12, 14, 9]

moradia_labels = ['Casa Própria', 'Alugada', 'Moradia Coletiva/Ocupação']
moradia_values = [55, 35, 10]

servicos_labels = ['Saneamento Básico', 'Água Potável', 'Energia Elétrica', 'Internet']
servicos_values = [85, 70, 90, 60]

# Configuração do layout
fig, axs = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle('Dados Demográficos da pesquisa amostral - Município de Feira de Santana', fontsize=16)

# Gráfico de Idade
axs[0, 0].pie(idade_values, labels=idade_labels, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
axs[0, 0].set_title('Distribuição por Idade')

# Gráfico de Gênero
axs[0, 1].pie(genero_values, labels=genero_labels, autopct='%1.1f%%', colors=['#ffcc99','#c2c2f0'])
axs[0, 1].set_title('Distribuição por Gênero')

# Gráfico de Renda
axs[1, 0].bar(renda_labels, renda_values, color=['#ff9999','#66b3ff','#99ff99'])
axs[1, 0].set_title('Distribuição de Renda')
axs[1, 0].set_ylabel('Percentual (%)')

# Gráfico de Ocupação
axs[1, 1].bar(ocupacao_labels, ocupacao_values, color=['#ffcc99','#c2c2f0','#ff6666', '#ffb3e6'])
axs[1, 1].set_title('Distribuição por Ocupação')
axs[1, 1].set_ylabel('Percentual (%)')

# Gráfico de Moradia
axs[2, 0].pie(moradia_values, labels=moradia_labels, autopct='%1.1f%%', colors=['#66b3ff','#99ff99','#ff9999'])
axs[2, 0].set_title('Tipo de Moradia')

# Gráfico de Acesso a Serviços
axs[2, 1].bar(servicos_labels, servicos_values, color=['#c2c2f0','#ff6666','#ffb3e6', '#66b3ff'])
axs[2, 1].set_title('Acesso a Serviços Básicos')
axs[2, 1].set_ylabel('Percentual (%)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()