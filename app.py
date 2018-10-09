
# importing  Flask (class) from flask.py (file) , so we get all methods and attributes of Flask class
from flask import Flask

#instantiating : creating an instance namely 'app' from class Flask, having a function Flask same as Flask class name
#  this special case is called as constructor because when ever function(method) name= class name, 
# argument passed __name__ is a global variable what ever name your file has will be printed 
#  now all the methods and attributes of flask will be in instance app

app = Flask(__name__)
# now we are making route of our instance 'app' by  placing @ before our instance name
# and then useing '.route' method with argument('/') showing current directory 

@app.route('/')
#  every route has a function  , here index function will return hello world


def index():
    return "Hello Wasim"

#app.run is method to run server /run this function
app.run(debug=True)






     