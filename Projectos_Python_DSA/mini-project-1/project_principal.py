# Importacão do panda, manipulação de dados e análise de dados por tabelas
import pandas as pd

# Importacão do matplotlib para visualização de dados graficamente
import matplotlib.pyplot as plt

# Importacão do seaborn para visualização de dados estatísticos
import seaborn as sns


# CARREGAR E EXPLORAR OS DADOS GERADOS NO ARQUIVO CSV
df_vendas = pd.read_csv('vendas.csv')


# Análise dos dados gerados
print("===== Análise dos Dados de Vendas =====")
print(df_vendas)

# Visualização das primeiras 5 linhas do DataFrame
print(df_vendas.head())
# Visualização das últimas 5 linhas do DataFrame
print(df_vendas.tail())
# Informações gerais sobre o DataFrame
print(df_vendas.info())
# Estatísticas descritivas do DataFrame
print(df_vendas.describe())


# LIMPEZA, PRE-PROCESSAMENTO E ENGENHARIA DE ATRIBUTOS
# Verificar valores ausentes
print("===== Verificação de Valores Ausentes =====")
print(df_vendas.isnull().sum())
print("===== Remoção de Valores Ausentes =====")
# Remover linhas com valores ausentes
df_vendas = df_vendas.dropna()

# Se a coluna 'Data_Pedido' estiver no formato de string, convertê-la para datetime
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

# Engenharia de atributos: Criar uma nova coluna 'Faturamento' calculando o faturamento total por venda
df_vendas['Faturamento'] = df_vendas['Quantidade_Venda'] * df_vendas['Preco_Unitario']

# Engenharia de atributos: Criar uma nova coluna 'status_Entrega' com base na região do estado
df_vendas['status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rapido' if estado in ['SP', 'RJ', 'MG'] else 'Normal')

print(df_vendas.info())
print(df_vendas)

# ANALISE 1: TOP 10 DOS PRODUTOS MAIS VENDIDOS
# Agrupar os dados por 'Nome_Produto' e somar a quantidade vendida
top_produtos = df_vendas.groupby('Nome_Produto')['Quantidade_Venda'].sum().sort_values(ascending=False).head(10)
print("===== Top 10 Produtos Mais Vendidos =====")
print(top_produtos)

# ANALISE 2: FATURAMENTO TOTAL POR PRODUTO
# Agrupar os dados por 'Nome_Produto' e somar o faturamento total
faturamento_produto = df_vendas.groupby('Nome_Produto')['Faturamento'].sum().sort_values(ascending=False)
print("===== Faturamento Total Por Produto =====")
print(faturamento_produto)

total_faturamento = faturamento_produto.sum()
print(f"Faturamento Total: R$ {total_faturamento:.2f}")

# Definir um estilo para os gráficos
# Definir um estilo para os gráficos
sns.set_style("whitegrid")


# ==============================
# GRÁFICO 1 - TOP 10 PRODUTOS
# ==============================

plt.figure(figsize=(10, 5))

top_produtos.sort_values(ascending=True).plot(
    kind='bar',
    color='skyblue'
)

plt.title('Top 10 Produtos Mais Vendidos', fontsize=16)
plt.ylabel('Quantidade Vendida', fontsize=14)
plt.xlabel('Nome do Produto', fontsize=14)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ==============================
# GRÁFICO 2 - FATURAMENTO POR PRODUTO
# ==============================

plt.figure(figsize=(10, 5))

faturamento_produto.sort_values(ascending=True).plot(
    kind='bar',
    color='lightgreen'
)

plt.title('Faturamento Total por Produto', fontsize=16)
plt.ylabel('Faturamento (R$)', fontsize=14)
plt.xlabel('Nome do Produto', fontsize=14)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


