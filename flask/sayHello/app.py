from flask import Flask, render_template, request, flash

app = Flask(__name__)  #creates a class for our app

@app.route("/hello")        #create a route for our app. e.g My domain.com/hello

def index():
    return render_template("index.html")




