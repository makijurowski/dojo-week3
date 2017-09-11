"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect, session
import random
import sys


app = Flask(__name__)
app.secret_key = "ninjazzzz"


@app.route('/')
def index():
    try:
        session['score'] += session['activity_score']
        session.pop('activity_score')
        session.pop('activity_text')
    except KeyError:
        session['score'] = 0
        session['activity_log'] = ''
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def location():
    if 'farm' in request.form:
        print ('Farm button clicked', file=sys.stderr)
        session['activity_score'] = random.randrange(10, 21)
        session['activity_text'] = 'You earned ' + str(session['activity_score']) + ' gold from the farm!\n'
        session['activity_log'] += session['activity_text']
        return redirect('/')
    elif 'cave' in request.form:
        print ('Cave button clicked', file=sys.stderr)
        session['activity_score'] = random.randrange(5, 11)
        session['activity_text'] = 'You earned ' + \
            str(session['activity_score']) + ' gold from the cave!\n'
        session['activity_log'] += session['activity_text']
        return redirect('/')
    elif 'house' in request.form:
        print ('House button clicked', file=sys.stderr)
        session['activity_score'] = random.randrange(2, 6)
        session['activity_text'] = 'You earned ' + \
            str(session['activity_score']) + ' gold from the house!\n'
        session['activity_log'] += session['activity_text']
        return redirect('/')
    elif 'casino' in request.form:
        print ('Casino button clicked', file=sys.stderr)
        session['activity_score'] = random.randrange(-50, 51)
        if session['activity_score'] >= 0:
            session['activity_text'] = 'You earned ' + \
                str(session['activity_score']) + ' gold from the casino!\n'
        elif session['activity_score'] < 0:
            session['activity_text'] = 'Oh no! You Lost ' + \
                str(session['activity_score']) + ' gold from the casino!\n'
        session['activity_log'] += session['activity_text']
        return redirect('/')
    else:
        print ('This did not work! :(')
        return render_template('index.html')

app.run(debug=True)
