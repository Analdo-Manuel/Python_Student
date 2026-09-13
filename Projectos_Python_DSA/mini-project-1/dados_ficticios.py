# Gerando dados Ficticios com Python

# Importacão do panda, manipulação de dados e análise de dados por tabelas
import pandas as pd

# Importacão do random para gerar números aleatórios e fazer escolhas aleatórias
import random

# Importacão do datetime para manipulação de datas e horas
from datetime import datetime, timedelta

# Importacão do numpy para operações matemáticas e manipulação de arrays
import numpy as np

def gerar_dados_ficticios(num_linhas = 600):
    print(f"\nIniciando a geração de {num_linhas} linhas de dados fictícios...\n")
    
    # Dicionario para armazenar os dados fictícios
    dados_ficticios = {
        'Laptop Gamer': {'Categoria': 'Eletrônicos', 'Preço': 3500.00, 'Estoque': 50, 'Vendas': 0},
        'Smartphone': {'Categoria': 'Eletrônicos', 'Preço': 2500.00, 'Estoque': 100, 'Vendas': 0},
        'Tablet': {'Categoria': 'Eletrônicos', 'Preço': 1500.00, 'Estoque': 75, 'Vendas': 0},
        'Monitor': {'Categoria': 'Eletrônicos', 'Preço': 800.00, 'Estoque': 60, 'Vendas': 0},
        'Teclado Mecânico': {'Categoria': 'Eletrônicos', 'Preço': 300.00, 'Estoque': 150, 'Vendas': 0},
        'Mouse Gamer': {'Categoria': 'Eletrônicos', 'Preço': 200.00, 'Estoque': 200, 'Vendas': 0},
        'Headset Gamer': {'Categoria': 'Eletrônicos', 'Preço': 400.00, 'Estoque': 120, 'Vendas': 0},
        'Cadeira Gamer': {'Categoria': 'Eletrônicos', 'Preço': 900.00, 'Estoque': 80, 'Vendas': 0},
        'SSD 1TB': {'Categoria': 'Eletrônicos', 'Preço': 600.00, 'Estoque': 90, 'Vendas': 0},
        'Placa de Vídeo': {'Categoria': 'Eletrônicos', 'Preço': 2000.00, 'Estoque': 40, 'Vendas': 0}
    }
    
    # criando uma lista com os nomes dos produtos
    list_produtos = list(dados_ficticios.keys())
    
    # Criar um Dicionario de cidade com os seus estados e regiões
    cidades = {
        'São Paulo': {'Estado': 'SP', 'Região': 'Sudeste'},
        'Rio de Janeiro': {'Estado': 'RJ', 'Região': 'Sudeste'},
        'Belo Horizonte': {'Estado': 'MG', 'Região': 'Sudeste'},
        'Curitiba': {'Estado': 'PR', 'Região': 'Sul'},
        'Porto Alegre': {'Estado': 'RS', 'Região': 'Sul'},
        'Salvador': {'Estado': 'BA', 'Região': 'Nordeste'},
        'Fortaleza': {'Estado': 'CE', 'Região': 'Nordeste'},
        'Recife': {'Estado': 'PE', 'Região': 'Nordeste'},
        'Manaus': {'Estado': 'AM', 'Região': 'Norte'},
        'Belém': {'Estado': 'PA', 'Região': 'Norte'}
    }    
    
    list_cidades = list(cidades.keys())

    # Lista que armazenará os registos de vendas
    registros_vendas = []
    
    # Definir uma data inicial para as vendas
    data_inicial = datetime(2026, 1, 1)
    
    # Loop para gerar os registos de vendas
    for i in range(num_linhas):
        # Escolher um produto aleatório
        produto = random.choice(list_produtos)
        
        # Escolher uma cidade aleatória
        cidade = random.choice(list_cidades)
        
        # Obter o estado e a região da cidade escolhida
        estado = cidades[cidade]['Estado']
        regiao = cidades[cidade]['Região']
        
        
        # Gerar uma quantidade de venda aleatória (entre 1 e 200)
        quantidade_venda = np.random.randint(1, 200)
        
        if quantidade_venda >= dados_ficticios[produto]['Estoque']:
            quantidade_venda = dados_ficticios[produto]['Estoque']
            
        data_pedido = data_inicial + timedelta(days=int(i/5), hours = random.randint(0, 23))
        
        if produto in ['Mouse Gamer', 'Curitiba']:
            preco_unitario = round(dados_ficticios[produto]['Preço'] * np.random.uniform(0.9, 1.0), 2)  # 10% de desconto
        else:
            preco_unitario = round(dados_ficticios[produto]['Preço'], 2)
            
        registros_vendas.append({
            'ID_Pedido': 100 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto,
            'Quantidade_Venda': quantidade_venda,
            'Preco_Unitario': preco_unitario,
            'Cidade': cidade,
            'Estado': estado,
            'Regiao': regiao
        })
    
    print("===== Registros de Vendas Gerados com Sucesso =====")
    df = pd.DataFrame(registros_vendas)
    df.to_csv('vendas.csv', index=False)
    df.to_excel('vendas.xlsx', index=False)
    return df
    
    
gerar_dados_ficticios(40)