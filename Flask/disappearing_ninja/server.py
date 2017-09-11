"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect, url_for
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja')
def ninja():
    return render_template('ninja.html')


@app.route('/ninja/<color>')
def colorchange(color):
    print ('The color chosen was: %s' % color, file=sys.stderr)
    stdColors = ['red', 'blue', 'orange', 'purple']
    if color in stdColors:
        return render_template('/ninja/' + color + '.html')
    else:
        return render_template('/ninja/missing.html')

app.run(debug=True)
# with app.test_request_context():
#    print url_for('colorchange', color)
