"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect, session, flash
import sys

app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    name = session['name']
    dojolocation = session['dojolocation']
    favlanguage = session['favlanguage']
    comments = session['comments']
    print ('New user input from form...', file=sys.stderr)
    print ('NAME: ' + name, file=sys.stderr)
    print ('DOJO LOCATION: ' + dojolocation, file=sys.stderr)
    print ('FAVORITE LANGUAGE: ' + favlanguage, file=sys.stderr)
    print ('COMMENTS: ' + comments, file=sys.stderr)
    return render_template('result.html', name=name, dojolocation=dojolocation,
                           favlanguage=favlanguage, comments=comments)


@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojolocation'] = request.form['dojo-location']
    session['favlanguage'] = request.form['fav-language']
    session['comments'] = request.form['comments']
    if len(session['name']) <= 0:
        flash('Please remember to enter your name.')
        return redirect('/')
    elif len(session['comments']) > 120:
        flash('Please do not enter more than 120 characters.')
        return redirect('/')
    else:
        # flash('Success! Your name is {}.'.format(session['name']))
        return redirect('/result')

app.run(debug=True)
