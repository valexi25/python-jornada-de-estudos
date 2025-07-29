print("*** Pedra Papel ou Tesoura ***")

jogador1 = "pedra"
jogador2 = "tesoura"

if jogador1 == jogador2:
    print("empate")
elif (jogador1 == 'pedra' and jogador2 =="tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra"):
    print("O jogador jogador1 Ganhou!! ")
else:
    print(f"O jogador jogador2 Ganhou!!! ")