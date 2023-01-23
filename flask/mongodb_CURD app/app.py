from flask import *
import subprocess as sp
from pymongo import *
import os

#from mongopass import mongopass

app = Flask(__name__) #creates Flask Class instance

mongopass = os.getenv("MONGOPASS") #get connection string from user enviroment variable
client = MongoClient(mongopass) #create mongo client instance to connect with MongoDB online Cluster
db = client.equipment_list #create a database
collection = db.bd #create a document collection

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
    date = sp.getoutput("date /t")
    time = sp.getoutput('time /t')
    type = request.args.get('type')
    notification = request.args.get('notification')
    equipment = request.args.get('equipment')
    description_equipment = request.args.get('description_equipment')
    description_problem = request.args.get('description_problem')
    cost_centre = request.args.get('cost_centre')
    reported_by = request.args.get('reported_by')
    myVal = {
    'Notif.date': date,
    'Notif. Time': time, 
    'Notifictn type': type, 
    'Notification': notification, 
    'Equipment': equipment,
    'Description_equipment': description_equipment,
    'Description_problem': description_problem,
    'Cost Center': cost_centre,
    'Reported by': reported_by,
    }
    x = collection.insert_one(myVal)
    return render_template('response.html', res = x)

#run flask app
if __name__ == "__main__":
    app.run(debug=True)










