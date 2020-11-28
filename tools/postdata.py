from config.configuration import db,collection

def insertamensaje(escena,personaje,frase):
    """
    función que inserta los datos en mongo es el momento de revisar que todos los datos
    estén como queramos. Eso os lo dejo a vosotras. Pero tenedlo en cuenta!! :rocket:
    """

    dict_insert = { "scene" : f"{escena}",
    "character_name" : f"{personaje}",
    "dialogue": f"{frase}"
    }
    collection.insert_one(dict_insert)