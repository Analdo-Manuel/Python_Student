# Criando um jogo de Pedra, Papel e Tesoura em Python multiplayer

print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
print("Regra: Pedra vence Tesoura, Tesoura vence Papel, Papel vence Pedra.")

nome_jogador1 = input("Digite o nome do Jogador 1: ")
nome_jogador2 = input("Digite o nome do Jogador 2: ")

opcoes = ["Pedra", "Papel", "Tesoura"]

valido = True

while valido:
    check = True
    while check:
        jogada_jogador1 = input(f"{nome_jogador1}, escolha sua jogada (Pedra, Papel ou Tesoura): ")
        jogada_jogador1 = jogada_jogador1.capitalize()

        if jogada_jogador1 not in opcoes:
            print("Jogada inválida para o Jogador 1!")
            continue
        while check:
            jogada_jogador2 = input(f"{nome_jogador2}, escolha sua jogada (Pedra, Papel ou Tesoura): ")
            jogada_jogador2 = jogada_jogador2.capitalize()
            if jogada_jogador2 not in opcoes:
                print("Jogada inválida para o Jogador 2!")
                continue
            else:
                check = False
    print(f"{nome_jogador1} escolheu: {jogada_jogador1}")
    print(f"{nome_jogador2} escolheu: {jogada_jogador2}")

    if jogada_jogador1 == jogada_jogador2:
        print("Empate!")
    elif (jogada_jogador1 == "Pedra" and jogada_jogador2 == "Tesoura") or (jogada_jogador1 == "Tesoura" and jogada_jogador2 == "Papel") or (jogada_jogador1 == "Papel" and jogada_jogador2 == "Pedra"):
        print(f"{nome_jogador1} venceu!")
    else:
        print(f"{nome_jogador2} venceu!")

    continue_jogo = input("Deseja continuar jogando? (s/n): ")
    if continue_jogo.lower() != "s":
        valido = False
