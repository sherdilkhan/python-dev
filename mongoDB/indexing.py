
from pymongo import *
from os 


mongopass = os.getenv("MONGOPASS") #get connection string from user enviroment variable
client = MongoClient(mongopass) #create mongo client instance to connect with MongoDB online Cluster
db = client.db_rm96_001 #create a database
collection_1 = db.bd #create a document collection

while True:
    date_stamp = sp.getoutput("date /t")
    time_stamp = sp.getoutput('time /t')
    v_l1n = instrument.read_float(registeraddress=19000, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals
    f = instrument.read_float(registeraddress=19050, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals 
    try:

        x = collection_1.insert_one(myVal)
    except:
        pass