import random
jogador = {}
jogadores = []

for x in range(0,3):
    jogador['nome'] = str(input(f'digite o nome do jogador {x}: '))
    jogador['dado'] = random.randint(1,6)
    if x == 0 or jogador['dado'] == jogadores[-1]['dado']:
        jogadores.append(jogador.copy())
    else:
        pos = 0
        while pos < len(jogadores):
            if jogador['dado'] <= jogadores[pos]['dado']:
                jogadores.insert(pos, jogador.copy())
                break
            else:
                pos += 1
        else:
            jogadores.append(jogador.copy())
    

print('VENCEDOR: ',jogadores[-1])


