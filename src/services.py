from models.cidade import Cidade
import db

def nova_cidade():
    cidade = Cidade(int(input('id: ')), input('nome: '), input('uf: '), int(input('total: '))) 
    db.cidades.append(cidade)

def msg_erro():
    print('Digitação inválida, tente novamente! Por favor, digite 1, 2, 3 ou 4!')

def num_casos(n,id):
    cidade_encontrada = None
    for o in db.cidades:
        if o.id == id:
            o.totaldecasos += n
            cidade_encontrada = o
            break
    if cidade_encontrada == None:
        print('A cidade solicitada não está cadastrada na nossa base de dados.')

def lista_cidades():
    for c in db.cidades:
        print(f'Cidade {c.nome} = {c.totaldecasos}')