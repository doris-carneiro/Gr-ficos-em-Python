import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/Users/Doris/Downloads/ecommerce_estatistica.csv')
print(df.head().to_string())

# Histograma - Parâmetros
# para entender a distribuição das principais métricas
plt.figure(figsize=(10, 6))
plt.hist(df['Nota'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição das Notas dos Produtos')
plt.xlabel('Notas')
plt.ylabel('Frequência')
plt.show()

# Gráfico de Dispersão
# para entender a relação entre variáveis numéricas
plt.scatter(df['Preço'], df['Qtd_Vendidos_Cod'], color='#5883a8', alpha=0.6, s=30)    #cor hexadecimal online
plt.title('Disperção entre Preço e Quantidade Vendida')
plt.xlabel('Preço (R$)')
plt.ylabel('Quantidade Vendida')
plt.show()

# Mapa de Calor
# para entender correlações entre variáveis numéricas
corr = df[['Preço', 'N_Avaliações']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Preço e N_Avaliações')
plt.show()

# Gráfico de barras
# comparar categorias ou grupos de forma clara e visual
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='skyblue')
plt.title('Qtde Vendida por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=30, ha='right')     # Rotaciona os nomes no eixo X
plt.show()

# Gráfico de pizza
# ideal para visualizar proporções
plt.figure(figsize=(8, 6))
plt.pie(y,
    labels=x,
    autopct='%1.1f%%',       # mostra os percentuais
    startangle=90)            # começa o gráfico no topo (90°)
plt.title('Distribuição de Vendas por Gênero')
plt.show()


# Gráfico de Densidade
# Visualizar a distribuição contínua de uma variável
# e entender onde há maior concentração de valores.
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='royalblue')
plt.title('Distribuição de Densidade dos Preços dos Produtos')
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.show()

# Gráfico de Regressão
# analisar relações entre variáveis numéricas
plt.figure(figsize=(10, 6))
sns.regplot(x='Preço', y='Qtd_Vendidos_Cod', data=df, scatter_kws={'alpha':0.7, 'color':'royalblue'})
plt.title('Relação entre Preço e Quantidade Vendida')
plt.xlabel('Preço (R$)')
plt.ylabel('Quantidade Vendida')
plt.show()

