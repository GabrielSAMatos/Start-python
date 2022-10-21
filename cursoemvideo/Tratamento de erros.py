try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a/b
except (ValueError, TypeError):
    print('Os dados fornecidos sao incompativeis')
except(ZeroDivisionError):
    print('Nao se pode dividir um numero por 0')
except KeyboardInterrupt:
    print('O usuario latiu e quitou')
else:
    print(c)
finally:
    print('Fim do programa')