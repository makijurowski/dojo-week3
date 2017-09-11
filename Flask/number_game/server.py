"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect, session, jsonify
import sys
import random


app = Flask(__name__)
app.secret_key = 'MuhKey'


@app.route('/')
def index():
    try:
        session['magic_number'] = session['magic_number']
    except KeyError:
        session['magic_number'] = random.randrange(0, 101)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def process_guess():
    session['guess'] = request.form['current_guess']
    print ('The current guess is: %i' % int(session['guess']), file=sys.stderr)
    session['magic_number'] = request.form['magic_number']
    print ('The magic number is: %i' % int(session['magic_number']),
           file=sys.stderr)
    check_guess()
    print ('Your result was: %s' % str(session['result']), file=sys.stderr)
    session.pop('guess')
    return redirect('/')


def check_guess():
    if session['guess'] < session['magic_number']:
        session['result'] = 'low'
        print('The current guess is too low.', file=sys.stderr)
    elif session['guess'] > session['magic_number']:
        session['result'] = 'high'
        print('The current guess is too high.', file=sys.stderr)
    elif session['guess'] == session['magic_number']:
        session['result'] = 'correct'
        session.pop('magic_number')
        session.pop('already_guessed')
        print('The current guess is correct!', file=sys.stderr)
    else:
        print('That did not work!', file=sys.stderr)
    # return session['result']
    result = session['result']
    return result


@app.route('/_get_result')
def get_result():
    result = session['result']
    return jsonify(result)


app.run(debug=True)
