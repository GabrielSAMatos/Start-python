def fatorial(num):
    f = 1 
    for i in range(1, num+1):
        f *= i
    return(f)


def somar(*num):
    s = 0
    for i in range(0, len(num)):
        s += num[i]
    return(s)


def subtrair(*num):
    princ = num[0]
    for i in range(1, len(num)):
        princ -= num[i]
    return(princ)


def dobro(num):
    return(num*2)


def triplo(num):
    return(num*3)


def metade(num):
    return(num/2)


def porcentagem(valor, taxa):
    if taxa == 0:
        return(valor)
    return(valor *(taxa/100))


def aumentar(valor, taxa):
    if taxa == 0:
        return(valor)
    return(valor*((taxa/100)+1))


def diminuir(valor, taxa):
    if taxa == 0:
        return(valor)
    return(valor-(valor*(taxa/100)))
    
