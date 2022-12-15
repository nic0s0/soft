from pymongo import MongoClient

def connectDb():

    cluster=MongoClient("mongodb+srv://admin:admin@arquisoft.pwcwcsp.mongodb.net/?retryWrites=true&w=majority")
    db=cluster["proyecto"]
    return db

data1 = {"nombre":"adfasdf","rut":"11111341-9", "fecha_caducidad":"2028-03-07"}

post1={"nombre":data1["nombre"], "rut":data1["rut"], "fecha_caducidad":data1["fecha_caducidad"]}
collection = connectDb()["usuarios"]

collection.insert_one(post1)