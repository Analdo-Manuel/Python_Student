# Criando uma Tupla em Python


cores = ("vermelho", "verde", "azul", "amarelo")

for cor in cores:
    print(cor)
    
print("-----------------------------")   
# Criando um dicionário em Python

cursos = {
    "Python": "Curso de Python",
    "Java": "Curso de Java",
    "JavaScript": "Curso de JavaScript"
}

for chave, valor in cursos.items():
    print(f"{chave}: {valor}")
    
print("-----------------------------")
# Criando um conjunto (set) em Python

linguagens = {"Python", "Java", "C++", "JavaScript"}

for linguagem in linguagens:
    print(linguagem)
    
print("-----------------------------")
# Criando uma lista em Python

frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(fruta)

print("-----------------------------")
# Contagem de 1 a 10 usando um loop for


for i in range(1, 11):
    print(i)

print("-----------------------------")
# Funcão

def soma_numeros(*args):
    return sum(args)

soma = soma_numeros(1, 2, 3, 4, 5)
print("Soma dos números: ", soma)  # Saída: Soma dos números:  15

print("-----------------------------")
# Lambda function

dobro = lambda x: x * 2
print("Dobro de 5: ", {dobro(5)})  # Saída: Dobro de 5:  10

numeros = [1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x ** 2, numeros))
print("Quadrados dos números: ", quadrados)  # Saída: Quadrados dos números:  [1, 4, 9, 16, 25]

quadrados_filtrados = list(filter(lambda x: x % 2 == 0, quadrados))
print("Quadrados pares: ", quadrados_filtrados)  # Saída: Quadrados pares:  [4, 16]

print("-----------------------------")
# Trabalhando com ramdom em Python

import random

provincias = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Paraná"]

print("Províncias: ", random.choice(provincias))

print("-----------------------------")

# Importar modulos com todos os dados
import modulo

msm = modulo.saudacao("analdo")
print(msm)
print(f"O valor de PI: {modulo.PI}")

# Importando algo especifico

from modulo import saudacao, PI

print(f"Valor de PI: {PI}")

