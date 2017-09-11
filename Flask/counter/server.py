"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect, session
import sys


app = Flask(__name__)
app.secret_key = 'COUNTMEUP'
myCount = 0


@app.route('/')
def index():
    try:
        session['count'] = session['count'] + 1
    except KeyError:
        session['count'] = 1
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def countbuttons():
    print ('The current count is: %i' % session['count'], file=sys.stderr)
    if 'add2' in request.form:
        session['count'] += 1
        return redirect('/')
    elif 'reset' in request.form:
        session['count'] = -1
        return redirect('/')
    else:
        print ('This did not work! :(')
        return render_template('index.html')


app.run(debug=True)
