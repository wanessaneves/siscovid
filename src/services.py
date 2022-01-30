from src.db import get_connection

from src.mappers import get_city_object, get_city_list

def nova_cidade(name, uf):
    connection, cursor = get_connection()
    cursor.execute(f"INSERT INTO cities (name, uf) VALUES('{name}', '{uf}')")
    connection.commit()
    connection.close()

def msg_erro():
    print('Digitação inválida, tente novamente! Por favor, digite 1, 2, 3 ou 4!')

def num_casos(id, quantidade):
    connection, cursor = get_connection()

    registers = cursor.execute(f"SELECT * FROM cities WHERE id = {id}")
    city_mapper = get_city_object(registers)

    if city_mapper == None:
        print('Cidade não encontrada')
        connection.commit()
        connection.close()

    else:
        city_mapper.add_total(quantidade)
        cursor.execute(f"UPDATE cities set total = {city_mapper.totaldecasos} WHERE id = {city_mapper.id}")
        connection.commit()
        connection.close()

def lista_cidades():
    connection, cursor = get_connection()
    registers = cursor.execute('SELECT * FROM cities')
    cities_mapper = get_city_list(registers)
    
    for c in cities_mapper:
        print(c.id, ' - ', c.nome, '/', c.uf, ' -> ', c.totaldecasos)
    connection.close()