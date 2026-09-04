# Declare uma variavel boolean chamado tm_carteira_motorista com valor true, imprime na tela a mensagem "Possui carteira de motorista: " seguido do valor da variavel tm_carteira_motorista.

import random

tm_carteira_motorista = [True, False]

num = bool(random.choice(tm_carteira_motorista))  # Gera um valor aleatório True ou False;

# Acessa o valor True na lista
if num:
    print("Possui carteira de motorista: ", tm_carteira_motorista[num])
else:
    print("Possui carteira de motorista: ", tm_carteira_motorista[num])