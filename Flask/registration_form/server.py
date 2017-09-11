"""This is a Coding Dojo homework assignment."""

from __future__ import print_function
from flask import Flask, render_template, request, redirect, session, flash
import sys
import re

NAME_REGEX = re.compile(r"^[a-zA-Z\\s]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASS_UPPER = re.compile(r"[A-Z{1,5}]")
PASS_DIGIT = re.compile(r"\d{1,5}")
# PASSWORD_REGEX = re.compile(r"[A-Z{1,5}]\|\d{1,5}")

app = Flask(__name__)
app.secret_key = 'SECRETS'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    flash('Your registration was successful!')
    return render_template('result.html')


@app.route('/process', methods=['POST'])
def process():
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    if len(session['email']) <= 0 or len(session['first_name']) <= 0 or \
        len(session['last_name']) <= 0 or len(session['password']) <= 0 or \
            len(session['confirm_password']) <= 0:
        flash('You must enter every field to continue.')
        return redirect('/')
    elif not NAME_REGEX.match(request.form['first_name']) or not NAME_REGEX.match(request.form['last_name']):
        flash('Please use only alphanumeric letters for your first and last name.')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address.')
        return redirect('/')
    elif len(session['password']) < 8:
        flash('Your password must be at least 8 characters in length.')
        return redirect('/')
    elif not PASS_UPPER.search(session['password']):
        flash('Passwords must contain one uppercase letter and one number.')
        return redirect('/')
    elif not PASS_DIGIT.search(session['password']):
        flash('Passwords must contain one uppercase letter and one number.')
        return redirect('/')
    elif session['password'] != session['confirm_password']:
        flash('The passwords do not match, please try again.')
        return redirect('/')
    else:
        return redirect('/result')

app.run(debug=True)
