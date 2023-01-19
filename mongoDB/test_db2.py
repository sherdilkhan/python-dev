import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ahl_equipment"]
mycol = mydb["hpdc"]

#for x in mycol.find():
    #print(x)

myquery = {"Equipment #": "800000426" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)