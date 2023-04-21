#!/usr/bin/python3
"""
    Basic falsk web application
"""
from flask import Flask


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
        functio for /hbnb url
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
