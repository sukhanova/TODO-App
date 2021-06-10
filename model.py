"""Models for todo app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    __tablename__ = "task"
    
    id = db.Column(db.Integer, 
                   autoincrement=True, 
                   primary_key=True)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, index=True, default=datetime.now())
    finished_at = db.Column(db.DateTime, index=True, default=None)
    is_finished = db.Column(db.Boolean, default=False)
    creator = db.Column(db.String, db.ForeignKey("users.username"))
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))

    def __init__(self, description, created_at=None, project_id=None, creator=None):
        self.description = description
        self.created_at = created_at or datetime.now()
        self.project_id = project_id
        self.creator = creator
        

    def __repr__(self):
        return f"<{self.status} Task: {self.description} by {self.creator or None}>"


    @property
    def status(self):
        return "finished" if self.is_finished else "open"

    def finished(self):
        self.is_finished = True
        self.finished_at = datetime.now()
        self.save()


    def to_dict(self):
        return {
            "description": self.description,
            "creator": self.creator,
            "created_at": self.created_at,
            "status": self.status,
        }

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