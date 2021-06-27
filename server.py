"""Functions for Lab Dashboard Tracking Task App."""

from flask import Flask, render_template, request, flash, session,redirect, abort, jsonify 
from model import User, Project, Task, ProjectTask, UserProject, connect_to_db, db
import os
from jinja2 import StrictUndefined


app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# ------- Guest Routes ------- :

@app.route('/')
def index():
    """View the homepage"""
    
    projects = Project.query.order_by(Project.title.asc()).all()
    return render_template("index.html",
                           projects=projects)


@app.route('/details', methods=['POST'])
def show_details():
    project_id = request.form.get("project_id")
    project = Project.query.get(project_id)
	
    return render_template("details.html", project=project, tasks=project.tasks)

  
@app.route('/about')
def show_about():
	"""About page"""

	return render_template('about.html')


@app.route('/register')
def register_user():
	"""User registration page"""

	return render_template("register.html")


@app.route('/login')
def login_form():
	"""User login page"""

	return render_template('login.html')


# ------- Auth Routes -------:

@app.route('/api/auth', methods=['POST'])
def login():
	user = User.query.filter_by(username=request.form.get('username')).first()

	if user.login(request.form.get('password')):
		app.logger.info('...Login successful.')
		session['user_id'] = user.user_id
	else:
		app.logger.info('-  Login failure  -')
		flash('Invalid username or password.')
		return render_template('login.html')

	return render_template('profile.html', user=user)


@app.route('/logout')
def logout():
	del session['user_id']

	return redirect('/')


@app.route('/api/register', methods=['POST'])
def register_auth():
	"""Handles user registration data"""

	app.logger.info('Registering new user...')

	user_data = dict(request.form)

	if user_data.get('password') == user_data.get('passwordConfirm'):
		del user_data['passwordConfirm']

		user = User(**user_data)
		user.create_password(user_data.get('password'))
		user.save()
		app.logger.info(f'New user {user.user_id} created. Logging in...')
		session['user_id'] = user.user_id

		return redirect(f'/users/{user.user_id}')


# ------- User Routes -------:

@app.route('/users/<int:user_id>')
def get_user(user_id):
	"""Shows users their profile page"""
	user = User.query.get(user_id)
	app.logger.info(f'Current user = {user}')

	return render_template('profile.html', user=user)


@app.route('/tasks')
def all_tasks():
    """Page with a list of all tasks"""
    
    tasks = Task.query.order_by(Task.status.desc()).all()
    
    return render_template('tasks.html', tasks=tasks)


@app.route('/new_task')
def new_task_form():
    
    return render_template('new_task.html')


@app.route('/create_task', methods=['POST'])
def create_task():
    
    app.logger.info('Creating new task...')
    
    task_data = dict(request.form)
    task = Task(**task_data)
    task.save()
    app.logger.info(f"New task {task.task_id} created. \nAdding to tasks page...")
    # redirect to tasks details page
    return redirect('/tasks')


#     print(project.tasks)
#     print("*"*10)

    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)