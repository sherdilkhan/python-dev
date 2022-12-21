# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, flash

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)  #creates a class for our app

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")        #create a route for our app. e.g My domain.com/hello

# ‘/’ URL is bound with index() function.
def index():
    return render_template("index.html")

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()


