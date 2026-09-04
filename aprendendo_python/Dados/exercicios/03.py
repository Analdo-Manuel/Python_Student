# Qual a diferença entra uma variavel de escopo local e uma variavel de escopo global? Dê um exemplo de cada uma.



num_global = 10  # Variável de escopo global

def exemplo_variavel_local():
    num_local = 5  # Variável de escopo local
    print("Variável local: ", num_local)  # Saída: 5
    print("Variável global dentro da função: ", num_global)  # Saída: 10
    
exemplo_variavel_local()
print("Variável global fora da função: ", num_global)  # Saída: