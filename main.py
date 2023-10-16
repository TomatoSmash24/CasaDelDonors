from os import name
from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

if name == 'main':
    app.run(debug=True)
