"""CRUD-related functions"""

from model import db, User, Project, Task, connect_to_db

def create_user(fname, lname, username, email, password):
    """Create and return a new user."""
    
    user = User(fname=fname,
                lname=lname,
                username=username,
                email=email,
                password=password)
    



if __name__ == '__main__':
    from server import app
    connect_to_db(app)