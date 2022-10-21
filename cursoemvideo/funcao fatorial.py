def fatorial(x, y=False):
    """
    -> Faz o fatorial de um numero
    para n: numero que deseja o fatorial
    para show=Sim: mostrara os calculos
    :return : retorna o fatorial de n   
    """
    fat = 1
    for numero in range(x, 0, -1):
        fat *= numero
        if y == True:
            if x == 1:
                print(f'{x} = ', end='')
            else:   
                print(f'{x} x ', end='')    
            x -= 1
    return(fat)
   

n = int(input('Fatorial de: '))
show = input('Quer ver o calculo? ').upper().strip()[0]
if show == 'S': show = True 
else: show = False
print(fatorial(n, show))
help(fatorial)