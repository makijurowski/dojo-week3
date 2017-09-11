"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    print ('New user from form: ' + name, file=sys.stderr)
    return redirect('/')

app.run(debug=True)
