segredo = 42

palpite = None

while segredo != palpite:
    palpite = int(input("Chute:"))
    if segredo == palpite:
        print("Ganhou o jogo!!")
