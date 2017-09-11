"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    dojolocation = request.form['dojo-location']
    favlanguage = request.form['fav-language']
    comments = request.form['comments']
    print ('New user input from form...', file=sys.stderr)
    print ('NAME: ' + name, file=sys.stderr)
    print ('DOJO LOCATION: ' + dojolocation, file=sys.stderr)
    print ('FAVORITE LANGUAGE: ' + favlanguage, file=sys.stderr)
    print ('COMMENTS: ' + comments, file=sys.stderr)
    # resultList = [{ 'name': name,
    #                 'dojolocation': dojolocation,
    #                 'favlanguage': favlanguage,
    #                 'comments': comments
    #                 }]
    return render_template('result.html', name=name, dojolocation=dojolocation,
                           favlanguage=favlanguage, comments=comments)

app.run(debug=True)
