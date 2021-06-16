"""CRUD-related functions"""
from datetime import datetime
from model import db, User, Project, Task, connect_to_db
    
def create_user(fname, lname, username, email, password):
    """Create and return a new user."""

    user = User(fname=fname,
                lname=lname,
                username=username,
                email=email,
                password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_project(title, description, start_date):
    """Create and return a new project."""
    
    project = Project(title=title, 
                      description=description, 
                      start_date=start_date, 
                      creator=creator)
    
    db.session.add(project)
    db.session.commit()

    return project


def create_task(user, project, description):
    """Create and return a new task."""
    
    task = Task(user=user, 
                project=project, 
                description=description)
    
    db.session.add(task)
    db.session.commit()

    return task


if __name__ == '__main__':
    from server import app
    connect_to_db(app)