"""Models for todo app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##############################################################################
# Model definitions

class User(db.Model):
    """A user."""

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
    """A project."""
    
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, 
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
    """A task."""
    
    __tablename__ = "tasks"
    
    id = db.Column(db.Integer, 
                   autoincrement=True, 
                   primary_key=True)
    description = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.now()
        

    def __repr__(self):
        return f"<{self.id} Task: {self.title}"


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