# Aprendendo Python - conjuntos (Sets)
# Conjuntos são coleções não ordenadas de elementos únicos. Eles são úteis para armazenar itens distintos e realizar operações matemáticas como união, interseção e diferença. Conjuntos são definidos usando chaves {} ou a função set().


# 1 - exemplo de conjunto

numeros = {1, 2, 3, 4, 5}
print("Conjunto de números: ", numeros)  # Saída: {1, 2, 3, 4, 5}

# 2 - exemplo de conjunto com elementos repetidos
numeros_repetidos = {1, 2, 2, 3, 3, 4, 4, 5, 5}
print("Conjunto de números repetidos: ", numeros_repetidos)  # Saída: {1, 2, 3, 4, 5}

numeros.add(6)  # Adicionando um elemento ao conxjunto
numeros_a = {7, 8, 9}
união = numeros.union(numeros_a)  # União de dois conjuntos
print("União de conjuntos: ", união)  # Saída: {1, 2, 3, 4, 5, 6, 7, 8, 9}

interseção = numeros.intersection(numeros_a)  # Interseção de dois conjuntos
print("Interseção de conjuntos: ", interseção)  # Saída: set()