from src.services import nova_cidade, num_casos, msg_erro, lista_cidades


run = True
while run:
    print('''
    Menu:
    1 - Cadastrar nova cidade
    2 - Cadastrar novos casos
    3 - Listar o total de casos
    4 - Para sair do sistema
    ''')
    acao = input('Digite a opção desejada: ')
    if acao not in '1234':
        msg_erro()
    elif acao == '1':
        nova_cidade() 
        print('Todas as cidades foram registradas com sucesso, obrigado(a) pela sua colaboração, continue se cuidando contra a Covid19. Até mais!')       
    elif acao == '2':
        id_cidade = int(input('Por favor digite o id da cidade: '))
        totalcasos = int(input('Agora digite o total de casos que você quer adicionar: '))
        num_casos(totalcasos, id_cidade)
    elif acao == '3':
        lista_cidades()
    elif acao == '4':
        print('Obrigado(a)!')
        run = False

