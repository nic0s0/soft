from pymongo import MongoClient

def connectDb():

    cluster=MongoClient("mongodb+srv://admin:admin@arquisoft.pwcwcsp.mongodb.net/?retryWrites=true&w=majority")
    db=cluster["proyecto"]
    return db