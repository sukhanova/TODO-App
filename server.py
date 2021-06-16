"""Functions for Lab Dashboard Tracking Task App."""

from flask import (Flask, render_template, request, flash, session,redirect)
from model import connect_to_db
import os
from jinja2 import StrictUndefined


app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """View the homepage"""
    return "<html><body>Placeholder for the homepage.</body></html>"


@app.route('/hello')
def say_hello():
    """Collect users first and last name."""

    return render_template("homepage.html")


@app.route('/welcome')
def greet_person():
    """Greet user by first and last name. Query database to pdisplay existing projects
    for choice buttons"""

    userFname = request.args.get("fname")
    userLname = request.args.get("lname")

    new_user = User(fname=userFname, lname=userLname)
    db.session.add(new_user)
    db.session.commit()

    projects = Project.query.all()
    


    return render_template("selectProject.html",
                           personFname=userFname,
                           personLname=userLname,
                           projects=projects
                           )


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)