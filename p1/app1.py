# P1  Hello World #
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLD!'

app.run(debug=True)