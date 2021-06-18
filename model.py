"""Models for todo app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##############################################################################
# Model definitions

class User(db.Model):
    """A user table in task_tracking database."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    username = db.Column(db.String, unique= True)
    email = db.Column(db.String, unique= True)
    password = db.Column(db.String)
    
    projects = db.relationship('Project', backref='users')
    
    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} username={self.username} email={self.email}>'

    
    
class Project(db.Model):
    """A project table in task_tracking database."""
    
    __tablename__ = 'projects'
    
    project_id = db.Column(db.Integer, 
                   autoincrement=True, 
                   primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    creator = db.Column(db.String, db.ForeignKey("users.username"))
    tasks = db.relationship("Task", backref="projects")


    def __init__(self, title=None, description=None, creator=None, start_date=None):
        self.title = title or "untitled"
        self.description = description or "untitled"
        self.creator = creator
        self.start_date = start_date or datetime.now()

    def __repr__(self):
        return f"<Project: {self.title} Description:{self.description} Start: {self.start_date}>"
    

    
class Task(db.Model):
    """A task table in task_tracking database."""
    
    __tablename__ = "tasks"
    
    task_id = db.Column(db.Integer, 
                   autoincrement=True, 
                   primary_key=True)
    description = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))

    def __init__(self, description, done):
        self.description = description
        self.done = False
        # self.pub_date = date.today()
        

    def __repr__(self):
        return f"<{self.id} Task: {self.title}"
    
    
class ProjectTask(db.Model):
    """project_task in task_tracking database."""
    
    __tablename__ = "projects_tasks"
    
    project_task_id = db.Column(db.Integer, 
                   autoincrement=True, 
                   primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.task_id"))


    def __repr__(self):
        return f"<ProjectTask project_task_id={self.project_task_id} project_id={self.project_id} task_id={self.task_id}>"



class UserTask(db.Model):
    """users_tasks table in task_tracking database."""

    __tablename__ = "users_tasks"

    user_task_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.task_id'))
    
    def __repr__(self):

        return f"<UserTask user_task_id={self.user_task_id} user_id={self.user_id} task_id={self.task_id}>"


class UserProject(db.Model):
    """users_projects table in task_tracking database."""

    __tablename__ = "users_projects"

    user_project_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))

    def __repr__(self):

        return f"<UserProject user_project_id={self.user_project_id} user_id={self.user_id} project_id={self.project_id}>"

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///task_tracking'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
    db.create_all()
    # db.drop()

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    print("Connected to DB!")