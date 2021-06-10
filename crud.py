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


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

    
def check_user_login_info(email, password):
    """Return users email and password match in database"""
    
    return User.query.filter((User.email == email) & (User.password == password)).first()


def get_all_users(): 
    """Returns all Users"""

    return User.query.all()


def get_user_info(user_id):
    """Returns user details"""
    return User.query.get(user_id)


def create_project(title, description, start_date):
    """Create and return a new project."""
    
    project = Project(title=title, 
                      description=description, 
                      start_date=start_date)
    
    db.session.add(project)
    db.session.commit()

    return project


def get_all_projects():
    """Return all projects."""

    return Project.query.all()


def get_project_by_id(project_id):
    """Return project by id"""
    
    return Project.query.get(project_id)


def create_task(description, created_at=datetime.now(), is_finished=False):
    """Create and return a new task."""
    
    task = Task(description=description)
    
    db.session.add(task)
    db.session.commit()

    return task


def get_all_tasks():
    """Return all tasks."""

    return Task.query.all()


def get_task_by_id(task_id):
    """Return task by id"""
    
    return Task.query.get(task_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)