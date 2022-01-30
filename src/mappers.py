from src.models.cidade import Cidade


# def get_city_object(registers, is_list=False):
#     city_mapper = [Cidade(row[0], row[1], row[2], row[3]) for row in registers]
#     return city_mapper if is_list else city_mapper[0]

def get_city_object(registers):
    city_mapper = None
    for row in registers:
        city_mapper = Cidade(row[0], row[1], row[2], row[3])
    return city_mapper

def get_city_list(registers):
    city_mapper = []
    for row in registers:
        obj = Cidade(row[0], row[1], row[2], row[3])
        city_mapper.append(obj)
    return city_mapper