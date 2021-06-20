"""Functions for Lab Dashboard Tracking Task App."""

from flask import Flask, render_template, request, flash, session,redirect
from model import User, Project, Task, ProjectTask, UserProject, connect_to_db, db
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

    return render_template("projects.html",
                           personFname=userFname,
                           personLname=userLname,
                           projects=projects
                           )


@app.route('/projects')
def select_project_form():
    """User choosing project they working on"""
    project_id = request.args.get("project")
    
    project = Project.query.get(project_id)
    
    return render_template("project_details.html", project=project)
    
   
@app.route('/projects/<project_id>')
def add_task(project_id):
    
    project = Project.query.get(project_id)
    # task = Task.query.get_all()
    task = ProjectTask.query.all()
    
    task_name = request.args.get('task')
    due_date = request.args.get('date')
    print(project.tasks)
    print("*"*10)
    # new_task = Task(description=task_name,
    #                 pub_date=date,
    #                 task_id=new_task_id)
    # db.session.add(new_task)
    # db.session.commit()
    
    
    # new_task_id = new_task.task_id
    # new_project_task = ProjectTask()
    # db.session.add(new_project_task)
    # db.session.commit()
    
    
    return render_template("project_details.html", 
                           description=task_name,
                           pub_date=due_date, 
                           project=project)
        

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)