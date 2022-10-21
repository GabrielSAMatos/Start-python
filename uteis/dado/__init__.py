def leiaDinheiro(msg):
    num = ''
    while not num.isalpha():
        num = input(msg).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'ERRO: {num} é um preço inválido')
        else:
            num = float(num)
            return(num)