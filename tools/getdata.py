from config.configuration import db, collection

def mensajepersonaje(nombre):
    """
    Hacemos una query a la base de datos para sacar las frases de un personaje
    """
    query = {"character_name":f"{nombre}"}
    frases = list(collection.find(query,{"_id":0, "scene":0}))
    return frases