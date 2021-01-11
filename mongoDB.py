#crear base de datos mongo
import pymongo
from bson.objectid import ObjectId #sirve para hacer referencia al object id

conn = pymongo.MongoClient("mongodb://localhost:27017/")

midb = conn["otraDb"]

miColleccion = midb["usuario"]

misColecciones = midb.list_collection_names() #colecciones que vamos a tener

# for x in misColecciones:
#     print(x)

# if "usuario" in misColecciones:
#     print("La coleccion de usuario si existe en la base de datos")
# else:
#     print("No existe")    
    
# usuario = {"nombre":"Bruno", "apellido":"Diaz","edad":35, "capa":True}

# r = miColleccion.insert_one(usuario)

# print("El id del documento es", r.inserted_id)
def insertar():
    usuarios = [{"nombre":"Ricardo", "apellido":"Diaz","edad":65, "capa":True},
            {"nombre":"Peter", "apellido":"Parker","edad":22, "capa":False},
            {"nombre":"Angel", "apellido":"fafa","edad":60, "capa":True}]

    r = miColleccion.insert_many(usuarios)

    return f"El numero de documentos(s) insertados(s): {r.inserted_ids}"

def select(one=False):
    if one == True:
        r = miColleccion.find_one()
        return r
    else:
        lista = []
        r = miColleccion.find()
        for n in r:
            lista.append(n)
        return lista    
    
def select_id(id):
    
    lista = []
    
    r = miColleccion.find({"_id": ObjectId(id)})
    
    for x in r:
        lista.append(x)
        
    return lista

def filtrar_datos(regex):
    r = miColleccion.find(regex)
    lista = []
    for x in r:
        lista.append(x)
    return x

def ordernar_datos(campo):
    #usamos sort para ordenar e indicamos el campo que ordenaria
    r = miColleccion.find({},{"_id":1, "nombre":1,"apellido":1,"edad":1}).sort(campo)# los que tienen 1 o 0 indican que queremos que muestre esos campos 0=false y 1=true
    lista = []
    for x in r:
        lista.append(x)
    
    return lista

def ordernar_por_mas_campos(campos):
    #usamos sort para ordenar e indicamos el campo que ordenaria
    lista=[]
    r = miColleccion.find({},{"_id":1, "nombre":1,"apellido":1,"edad":1}).sort([(campos[0],-1),(campos[1], 1)])# el 1 indica asc y el -1 indica desc
    for x in r:
        lista.append(x)
    
    return lista

def limitar_datos(cantidad):
    lista = []
    r = miColleccion.find().limit(cantidad)
    for x  in r:
        lista.append(x)
    return lista

def update_datos(query_to_update, query_update):
    try:
        miColleccion.update_one(query_to_update,query_update)
        return True
    except Exception as e:
        return False

def remove_one_data(query):
    try:
        miColleccion.delete_one(query)
        return True
    except Exception as e:
        return False, e
    
def remove_many_data(query):
    try:
        miColleccion.delete_many(query)
        return True
    except Exception as e:
        return False, e

def remove_colect(nombreCol):
    misColecciones = midb.list_collection_names()
    for x in misColecciones:
        print(x)
    miColleccion = midb[nombreCol]
    miColleccion.drop()
    misColecciones = midb.list_collection_names()
    for x in misColecciones:
        print(x)

if __name__ == "__main__":
    pass
    # insertar()
    # print(select(one=False))    
    # print(select_id("5ffc65a3e7c5a438513295d5"))
    # print(filtrar_datos({"nombre":{"$gt":"P"}})) #todos los que en el diccionario empiecen con una letra mayor a P
    # print(filtrar_datos({"nombre":{"$eq":"Bruno"}}))
    # print(filtrar_datos({"nombre":{"$regex":"^j"}})) #todos los que empiecen con J  
    # print(filtrar_datos({"nombre":{"$regex":"^P"}}))    
    # print(ordernar_datos("nombre"))
    # print(ordernar_por_mas_campos(["edad","nombre"]))
    # print(limitar_datos(2))
    # print(update_datos({"nombre":"josejose"},{"$set":{"nombre":"Jorge"}}))
    # print(select(one=False))
    # print(remove_one_data({"nombre":"Peter"}))
    # print(remove_one_data({"nombre":{"regex":"^R"}})) #elimina el primero con r
    # print(select(one=False))
    # print(remove_many_data({"capa":True})) #elimina todos los datos que posean capa:true
    # print(select(one=False))
    #remove_colect("musica")
    