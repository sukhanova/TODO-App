"""Script to seed database."""
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

from model import db, User, Project, Task, connect_to_db
from server import app

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load users data from JSON file
with open('data/users.json') as users_file:
    user_data = json.loads(users_file.read())
    
# Load projects data from JSON file
with open('data/projects.json') as projects_file:
    project_data = json.loads(projects_file.read())

# Load tasks data from JSON file
with open('data/tasks.json') as tasks_file:
    task_data = json.loads(tasks_file.read())
    
    
# Create projects, store them in list so we can use them
# to create tasks   
projects_in_db = []
for project in project_data:
    title, description, creator = (project['title'],
                                   project['description'],
                                   project['creator'])
    start_date = datetime.strptime(project['start_date'], '%Y-%m-%d')
    
    db_project = crud.create_project(title, description, start_date, creator)
    
    project_in_db.append(db_project)

        
if __name__ == "__main__":
    from flask import Flask
    connect_to_db(app)
    db.drop_all()
    db.create_all()
    

    create_users()
    create_projects()
    create_tasks()
    
    db.session.commit()