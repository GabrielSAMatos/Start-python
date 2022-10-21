def ajuda(com):
    help(com)


while True:
    comando = input('Funcao ou Biblioteca > ')
    if comando == 'fim':
        break
    else:
        ajuda(comando)