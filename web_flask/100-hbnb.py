#!/usr/bin/python3
"""
    Basic falsk web application
"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.user import User

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    """
        list of all State objects present
    """
    states = list(storage.all('State').values())
    amenities = list(storage.all('Amenity').values())
    places = list(storage.all('Place').values())
    cities = list(storage.all('City').values())
    users = list(storage.all('User').values())
    # print('========Debuging session============')
    # print(type(places[0]))
    # for walla in users:
    #     if walla.id == 'fa44780d-ac48-41ab-9dd0-ac54a15755cf':
    #         print(walla.first_name)
    # print('====================================')
    return render_template('100-hbnb.html', tasks=states, amenities=amenities, places=places, users=users)


@app.teardown_appcontext
def teardown(self):
    """
        After each request you must remove the current session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
