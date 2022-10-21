def leiaint(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: favor digitar inteiro valido.')
            continue
        else:
            return n


def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: favor digitar um real')
            continue
        else:
            return n