
#Sure, here's an example Flask route that receives the form data and sends it to
# a MySQL database using the mysql-connector-python package:

import smtplib
from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Define MySQL database connection details
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql123",
  database="my_website"
)

# Define a function to insert data into MySQL database
def insert_data(name, email, gender, interests, datetime):
    mycursor = mydb.cursor()
    sql = "INSERT INTO user_data (name, email, gender, interests, datetime) VALUES (%s, %s, %s, %s, %s)"
    val = (name, email, gender, interests, datetime)
    mycursor.execute(sql, val)
    mydb.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data_enter')
def data_enter():
    return render_template('data_enter.html')

@app.route('/contact')
def home():
    return render_template('contact.html')

@app.route('/aboutUs')
def about_us():
    return render_template('aboutUs.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # email body
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    # send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_email_password")
        server.sendmail("your_email@gmail.com", "your_personal_email@gmail.com", body)
        server.quit()
        return render_template('success.html')
    except:
        return render_template('failure.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    interests = ','.join(request.form.getlist('interests'))
    datetime = request.form['datetime']
    insert_data(name, email, gender, interests, datetime)
    return 'Data inserted successfully.'

@app.route('/data_display')
def data_display():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM user_data")
  data = mycursor.fetchall()
  return render_template('data_display.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)


#In this example, we defined a function insert_data to insert the form
#data into a MySQL database using the mysql-connector-python package. 
#The submit route receives the form data and calls this function to 
#insert the data into the database.
