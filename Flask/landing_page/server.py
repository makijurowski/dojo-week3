"""This is a Coding Dojo homework assignment."""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dojos/new')
def dojos():
    return render_template('dojo.html')

@app.route('/dojos/new', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    print name
    print email
    return redirect('/dojos/new')  

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

app.run(debug=True)
