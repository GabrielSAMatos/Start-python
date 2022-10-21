def notas(nota, sit=False):
    boletim ={}
    boletim['total'] = len(nota)
    boletim['maior'] = max(nota) 
    boletim['menor'] = min(nota) 
    boletim['media'] = sum(nota)/len(nota)
    if sit:
        if (boletim['media']) >= 7:
            boletim['situacao'] = 'Aprovado'
        elif (boletim['media']) > 4:
            boletim['situacao'] = 'Recuperacao'
        else: 
            boletim['situacao'] = 'Reprovado'
    return(boletim)


provas =[]
qnt = int(input('Quantas provas? '))
for i in range(qnt):
    provas.append(float(input(f'Prova {i+1}: ')))
sit = input('Deseja saber se o aluno passou? ').lower()[0]
if sit == 's':
    sit = True 
else:
    sit = False
resp = notas(provas, sit)
print(resp)