
import time
from pymongo import *
import os
import subprocess as sp

mongopass = os.getenv("MONGOPASS") #get connection string from user enviroment variable
client = MongoClient(mongopass) #create mongo client instance to connect with MongoDB online Cluster
db_rm96_001 = client.db_rm96_001 #create a database
collection_1 = db_rm96_001.collection_1 #create a document collection

while True:
    date_stamp = sp.getoutput("date /t")
    time_stamp = sp.getoutput('time /t')
    try:
        myVal = {
        'date': date_stamp,
        'time': time_stamp,
        'v_l1n': '240',
        'frequency': '50' 
        }
        x = collection_1.insert_one(myVal)
    except:
        pass
    time.sleep(.1)
    

    
