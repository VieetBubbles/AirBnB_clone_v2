#!/usr/bin/python3
# Write a script that starts a Flask web application

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def teardown_tempal():
    return (render_template('7-states_list.html', states=storage.all('State')))


@app.route("/cities_by_states", strict_slashes=False)
def list_cities():
    return (render_template('8-cities_by_states.html',
                            states=storage.all('State'),
                            cities=storage.all('City')))

if __name__ is "__main__":
    app.run(host="0.0.0.0", port=5000)
