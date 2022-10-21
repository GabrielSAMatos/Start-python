poupanca = 0
deposito = 100
for i in range(24):
    if i < 12:
        poupanca += deposito 
        deposito += 10
    else: 
        poupanca = ((poupanca + deposito)*1.1)
        deposito += 10 

print(f'2 ano mais rendendo 10%: {poupanca}' )


