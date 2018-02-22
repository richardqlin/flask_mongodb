
from pymongo  import  MongoClient

client=MongoClient('mongodb://127.0.0.1:27017')


print('mongo file')
db=client.planets

db.planets.insert_one({'name': 'Earth', 'color': 'blue'})
db.planets.insert_many([{'name': 'Mars', 'color': 'red'},
                     {'name': 'Saturn', 'color': 'yellow'},
                     {'name': 'Pluto', 'color': 'brown'}])

print('mongo file')
for document in db.planets.find():
    print (document)