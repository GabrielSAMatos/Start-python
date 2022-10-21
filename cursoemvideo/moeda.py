def resumo(valor, aum, red):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aum}% de aumento: \t{aumentar(valor, aum, True)}')
    print(f'{red}% de reducao: \t\t{diminuir(valor, red, True)}')
    print(f'-'*35)


def somar(*valor, format=False):
    resp = 0
    for i in range(0, len(valor)):
        resp += valor[i]
    return resp if format is False else moeda(resp)


def subtrair(*valor, format=False):
    resp = valor[0]
    for i in range(1, len(valor)):
        resp -= valor[i]
    return(resp) if format is False else moeda(resp)


def dobro(valor, format=False):
    resp = valor*2
    return(resp) if format is False else moeda(resp)


def triplo(valor, format=False):
    resp = valor*3
    return(resp) if format is False else moeda(resp)


def metade(valor, format=False):
    resp = valor/2
    return(resp) if format is False else moeda(resp)


def porcentagem(valor, taxa, format=False):
    if taxa == 0:
        return(valor) if format is False else moeda(valor)
    resp = valor *(taxa/100)
    return(resp) if format is False else moeda(resp)


def aumentar(valor, taxa, format=False):
    if taxa == 0:
        return(valor) if format is False else moeda(valor) 
    resp = valor*((taxa/100)+1)
    return(resp) if format is False else moeda(resp)


def diminuir(valor, taxa, format=False):
    if taxa == 0:
        return(valor) if format is False else moeda(valor)
    resp = valor-(valor*(taxa/100))
    return(resp) if format is False else moeda(resp)


def moeda(valor=0, moeda='R$'):
    return(f'{moeda}{valor:.2f}'.replace('.',','))


