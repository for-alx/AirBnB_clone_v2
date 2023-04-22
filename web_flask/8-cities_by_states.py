#!/usr/bin/python3
"""
    Basic falsk web application
"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """
        web root content
    """
    states = list(storage.all('State').values())
    # print("=====================================================")
    # print(states[0].cities)
    # # print(states[0])
    # print("=====================================================")
    return render_template('8-cities_by_states.html', tasks=states)


@app.teardown_appcontext
def handle_teardown(self):
    """
        After each request you must remove the current session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
