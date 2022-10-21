def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')


n = input('Nome: ')
g = input('Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
