#!/usr/bin/python3
# Write a script that starts a Flask web application

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    storage.close()

@app.route("/states", strict_slashes=False)
@app.route("/states_list", strict_slashes=False)
def teardown_tempal():
    return (render_template('7-states_list.html', states=storage.all('State')))


@app.route("/cities_by_states", strict_slashes=False)
def list_cities():
    return (render_template('8-cities_by_states.html',
                            states=storage.all('State'),
                            cities=storage.all('City')))


@app.route("/states/<id>", strict_slashes=False)
def inherit_state(id):
    """Return a state object so html file can use cities within state"""
    states_list = storage.all('State').values()
    for state in states_list:
        if state.id == id:
            return (render_template('9-states.html',
                                    state=state))
    return (render_template('9-states.html',
                            state=None))

if __name__ is "__main__":
    app.run(host="0.0.0.0", port=5000)
