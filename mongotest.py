import pymongo
client = pymongo.MongoClient("mongodb+srv://Suchit:<G&alfthegr8!>@suchit.osq2tcv.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"Suchit",
    "email":"suchit.skulkarni@gmail.com",
    "surname":"Kulkarni"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)