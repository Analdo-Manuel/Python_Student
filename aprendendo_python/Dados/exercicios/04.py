# Crie uma variavel chamada saldo com valor 500,50(float), Em seguida, cria uma variavel saque com valor 200,25(float). Subtraia o valor do saque do saldo e exiba o resultado na tela.

while True:
    saldo = float(input("Digite o saldo inicial: "))
    saque = float(input("Digite o valor do saque: "))

    if saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= saque
        print("Saldo após o saque: ", saldo)
        break