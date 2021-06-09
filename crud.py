"""CRUD-related functions"""
import random
# from datetime import datetime
from model import db, User, Project, Task, connect_to_db

# def create_user(fname, lname, username, email, password):
#     """Create and return new user."""
    
#     user = User(fname=fname,
#                 lname=lname,
#                 username=username,
#                 email=email,
#                 password=password)
    
#     db.session.add(user)
#     db.session.commit()
    
#     return user

# def create_project(title, description, start_date):
#     """Create and return a project."""
    
#     project = Project(title=title,
#                       description=description,
#                       start_date=start_date)
    
    
# def create_task(description, )

class DataGenerator:
    def __init__(self):
        db.drop_all()
        db.create_all()
        
    def create_users(self, count):
        for _ in range(count):
            User(
                fnane=forgery_py.name.first_name(),
                lname=forgery_py.name.last_name(),
                username=forgery_py.internet.user_name(True),
                email=forgery_py.internet.email_address(),
                password="todoapptest",
            ).save()
               
    # def create_projects(self, count):
    #     # for creator relations in db 
    #     users = Users.query.all()
    #     assert users !=[]
    #     for _ in range(count):
    #         Project(
    #             title=title,
    #             description=description,
    #             start_date=start_date
    #             creator=random.choice(users).username
    #         ).save()
            
    # def create_tasks(sel, count):
    #     # for project relations in db
    #     projects = Project.query.all()
    #     assert projects !=[]
    #     for _ in range(count):
    #         project = random.choice(projects)
    #         task=Task(
    #             description=description,
    #             created_at=self.generate_fake_date().save()
    #             creator=project.creator,
    #             project_id=project_id
    #         ) .save()
            
    
    def generate_data(self, count):
        self.create_users(count)
        # self.create_projects(count *3)
        # self.create_tasks(count *12)   
    
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)