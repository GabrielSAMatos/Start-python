def cabecalho_centralizado(msg):
    print('-'*42)
    print(f'{msg:^42}')    
    print('-'*42)


def printopcoes(opcs):
    for i in range(len(opcs)):
        print(f'{i+1} - {opcs[i]}')



def printmenu():
        cabecalho_centralizado('MENU PRINCIPAL')
        printopcoes(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair'])
        print('-'*42) 


def menu():
    while True:
        printmenu()
        erro = True
        while erro:
            erro = selecione()
            

        
def selecione():
    msg = ('Sua opção: ')
    try:
        opc = int(input(msg))
        if opc == 1 or opc == 2 or opc == 3:
            if opc == 1:
                cabecalho_centralizado('PESSOAS CADASTRADAS')
                with open("Cadastrados.txt", "r") as arquivo:
                    linhas = arquivo.readlines()
                    if len(linhas) == 0:
                        print('Não há pessoas cadastradas ainda!')
                    for linha in linhas:
                        print(linha, end='')
                return False
            if opc == 2:
                cabecalho_centralizado('CADASTRAR PESSOA')
                cadastro()
                return False
            if opc == 3:   
                exit()        
        elif  opc < 1 or opc > 3:
            print('ERRO! Digite uma opção válida!')
    except(ValueError):
        print('ERRO! Favor digitar um numero!')
        return True
    except(KeyboardInterrupt):
        print('\nERRO! Digite uma opção válida!')
       
def cadastro():
    cadastrados = open('Cadastrados.txt', 'a')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cadastrados.write(f'{nome:<28} {idade} anos\n')
    cadastrados.close()
    print(f'Novo registro de {nome} adicionado.')
    

                
menu()
