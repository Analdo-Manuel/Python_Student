# Aprendendo Dicionários em Python
# Dicionários são estruturas de dados que armazenam pares de chave-valor. Cada chave é única e é usada para acessar o valor correspondente. Dicionários são definidos usando chaves {}.

# 1 - exemplo de dicionário

pessoa = {
    "nome": "Analdo Silva",
    "idade": 30,
    "cidade": "Luanda", 
    "filme_favorito": "Inception",
    "activo": True
}

print("Informações da pessoa: ", pessoa)  # Saída: {'nome': 'Analdo Silva', 'idade': 30, 'cidade': 'Luanda'}
print("Nome: ", pessoa["nome"])  # Saída: Analdo Silva
print("Idade: ", pessoa.get("idade"))   # Saída: 30
print("Cidade: ", pessoa.items())  # Saída: Luandaclear
