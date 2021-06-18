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
    return "<html><body>Placeholder for the homepage</body></html>"


@app.route('/welcome')
def say_hello():
    """Collect users first and last name."""

    return render_template("homepage.html")


@app.route('/greet')
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


@app.route('/selectProject')
def select_project_form():
    """User choosing project they working on"""
    project_id = request.args.get("project")
    
    project = Project.query.get(project_id)
    
    return render_template("project_details.html", project=project)
    
    
    

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)