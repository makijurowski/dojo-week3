"""This is a Coding Dojo homework assignment."""

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def hello():
    return render_template('index.html')
app.run(debug=True)

@app.route('/success')
def success():
    return render_template('success.html')
