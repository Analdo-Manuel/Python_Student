# Tudo Sobre Listas em Python
# Lista pode conter qualquer tipo de dado, incluindo outras listas. As listas são mutáveis, o que significa que você pode alterar seus elementos após a criação. (Mutavel significa que você pode alterar os elementos da lista após a criação.)

fruit = ["apple", "banana", "cherry"]

# sistema de indexação
for index in fruit:
    print(index)

# apresta a lista
print("Lista completa:", fruit)

# adiciona um item no final da lista
fruit.append("orange")
print("Lista após adição de 'orange':", fruit)

# insere um item em uma posição específica
fruit.insert(1, "kiwi")
print("Lista após adição de 'orange' e inserção de 'kiwi':", fruit)

# remove um item da lista   
fruit.remove("banana")

print("Lista após remoção de 'banana':", fruit)

# remove o último item da lista
fruit.pop()
print("Lista após remoção do último item:", fruit)