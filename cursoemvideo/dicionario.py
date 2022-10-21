time = []
while True: 
    gols = []
    jogadores = {}
    jogador = input('Digite o nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador} jogou?'))
    jogadores['jogador'] = jogador
    jogadores['partidas'] = partidas
    tot = 0
    for i in range(partidas):
        jogadores['gols'] = int(input(f'Quantos gols fez na partida {i}?'))
        tot += jogadores['gols']
        gols.append(jogadores['gols'])
        jogadores['gols'] = gols
    jogadores['tot'] = tot
    time.append(jogadores)

    s = input('Deseja continuar? ').upper().strip()[0]
    while s != 'S' and s != 'N':
        print('Error, Digite SIM OU NAO!')
        s = input('Deseja continuar? ').upper().strip()[0]
    if s == 'N':
        break

print('-='*40)
print(f'{"cod":>3} {"nome":>3} {"gols":>13} {"total":>16}')
print('-'*42)
for i, jogador in enumerate(time):
    print(f'{i:<3} {jogador["jogador"]:<13} {str(jogador["gols"]):<15} {jogador["tot"]:<10} ')
print('-'*42)

while True:
    dados = int(input('Quer mostrar os dados de qual jogador? (999 para parar) '))
    while dados >= len(time) and dados != 999:
        print(f'ERRO, nao existe jogador com codigo {dados}')
        dados = int(input('Quer mostrar os dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[dados]["jogador"]}:')
        for jogo, gol in enumerate(time[dados]['gols']):
            print(f'No jogo {jogo+1} fez {gol} gols')
print('Fim inferno cao praga')