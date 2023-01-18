import pymongo  #import mongo library

# creation of MongoClient
#client=pymongo.MongoClient()
  
# Connect with the portnumber and host
client = pymongo.MongoClient('mongodb://localhost:27017')

# Access database
mydatabase = client['testDb']

# Access collection of the database
mycollection = mydatabase[myTable]

# dictionary to be added in the database
rec = { "name": "John", "address": "Highway 37" }
# inserting the data in the database
rec = mydatabase.myTable.insert(rec)