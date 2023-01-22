from flask import *
import subprocess as sp
from pymongo import *
import os
#from mongopass import mongopass

app = Flask(__name__) #creates Flask Class instance

mongopass = os.getenv("MONGOPASS") #get connection string from user enviroment variable
client = MongoClient(mongopass) #create mongo client instance to connect with MongoDB online Cluster
db = client.ahl_equipment
collection = db.bd

#Lets create URL Mapping for different html pages

@app.route('/')
def home_page():
    date = sp.getoutput("date /t")
    return render_template("home.html", date = date )

@app.route('/curd')
def curd_page():
    return render_template('curd.html')

@app.route('/read')
def read():
    cursor = collection.find()
    for record in cursor:
        name = record['Notification']
        print(name)
        return render_template('response.html', res = name)


#run flask app
if __name__ == "__main__":
    app.run(debug=True)










