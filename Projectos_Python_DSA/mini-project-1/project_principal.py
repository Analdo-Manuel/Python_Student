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