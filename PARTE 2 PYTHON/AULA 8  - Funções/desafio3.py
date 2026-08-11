def ficha(nome='desconhecido', gol=0):
    print( f'o jogador {nome} marcou {gols} no campeonato!')

nome = str(input('digite o nome do jogador: '))
gols = str(input('digite o numero de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)

else:
    ficha(nome,gols)


