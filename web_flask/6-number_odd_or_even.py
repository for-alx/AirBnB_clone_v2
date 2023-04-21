#!/usr/bin/python3
"""
    Basic falsk web application
"""
from flask import Flask, escape, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
        web root content
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        function for /hbnb url
    """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """
        accepting text input
    """
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """
        Python function
    """
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    """
        accepting url parameter(number)
    """
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """
        Template usage
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
        check if number is odd or even
    """
    result = {'no': n}
    if n % 2 == 0:
        result['type'] = 'is even'
        return render_template('6-number_odd_or_even.html', number=result)
    result['type'] = 'is odd'
    return render_template('6-number_odd_or_even.html', number=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
