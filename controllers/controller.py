import web
from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin@iot-shard-00-00.usvse.mongodb.net:27017,iot-shard-00-01.usvse.mongodb.net:27017,iot-shard-00-02.usvse.mongodb.net:27017/serviceIot?ssl=true&replicaSet=atlas-75tzdc-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
db2 = client.gettingStarted
people = db.people
a2 = people.find_one({ "name.last": "Turing" })
class Control:
    def GET(self, name):
        if not name:
            name = 'World'
        return a2