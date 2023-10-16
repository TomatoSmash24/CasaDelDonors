
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('Home Page.html')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/toys')
def toys():
    return render_template('toys.html')

@app.route('/money')
def money():
    return render_template('money donations.html')

@app.route('/household')
def household():
    return render_template('household.html')

if __name__ == 'main':
    app.run(debug=True)
