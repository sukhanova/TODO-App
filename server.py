"""Functions for Lab Dashboard Tracking Task App."""

from flask import (Flask, render_template, request, flash, session,redirect)
from model import connect_to_db
import os
from jinja2 import StrictUndefined


app = Flask(__name__)
#os.enviorn -> use this to replace the actual key
#don't forget to run source secrets.sh in terminal!!

# app.secret_key = os.environ['SECRET_KEY']
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """View the homepage"""
    return "<html><body>Placeholder for the homepage.</body></html>"


@app.route('/welcome')
def say_hello():
    """Welcome user and get first and last name."""

    return render_template("homepage.html")


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)