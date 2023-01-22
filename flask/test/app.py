from flask import *
import subprocess as sp
from pymongo import *
import os
#from mongopass import mongopass

app = Flask(__name__) #creates Flask Class instance

mongopass = os.getenv("MONGOPASS") #get connection string from user enviroment variable
client = MongoClient(mongopass) #create mongo client instance to connect with MongoDB online Cluster
db = client.sherdil_inv
collection = db.tools

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
        notification = record['Notification']
        print(notification)
        return render_template('response.html', res = notification)

@app.route('/insert')
def insert():
    notification = request.args.get('notification')
    equipment = request.args.get("equipment")
    myVal = {'notification': notification, 'equipment': equipment }
    x = collection.insert_one(myVal)
    return render_template('response.html', res = x)


#run flask app
if __name__ == "__main__":
    app.run(debug=True)










