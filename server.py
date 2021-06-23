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
	"""Renders description and details in place on index.html"""

	project_title = request.form.get('project_title')

	project = Project.query.filter(Project.title==project_title).first()

	return jsonify({'name': project.title, 
				    'description': project.description,
                    'start_date': project.start_date})
 
 
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


@app.route('/projects')
def select_project_form():
    """User choosing project they working on"""
    project_id = request.args.get("project")
    
    project = Project.query.get(project_id)
    
    return render_template("project_details.html", project=project)




# @app.route('/greet')
# def greet_person():
#     """Greet user by first and last name. Query database to pdisplay existing projects
#     for choice buttons"""

#     userFname = request.args.get("fname")
#     userLname = request.args.get("lname")

#     new_user = User(fname=userFname, lname=userLname)
#     db.session.add(new_user)
#     db.session.commit()

#     projects = Project.query.all()

#     return render_template("projects.html",
#                            personFname=userFname,
#                            personLname=userLname,
#                            projects=projects
#                            )

# @app.route('/projects')
# def select_project_form():
#     """User choosing project they working on"""
#     project_id = request.args.get("project")
    
#     project = Project.query.get(project_id)
    
#     return render_template("project_details.html", project=project)

   
# @app.route('/projects/<project_id>')
# def display_tasks(project_id):
    
#     project = Project.query.get(project_id)
#     task = ProjectTask.query.all()
    
#     description = request.args.get("task")
#     status = request.args.get("status")
#     print(project.tasks)
#     print("*"*10)
    
    
#     # new_task = Task(description=task,
#     #                 status=status,
#     #                 task_id=new_task_id)
#     # db.session.add(new_task)
#     # db.session.commit()
    
    
#     # new_task_id = new_task.task_id
#     # new_project_task = ProjectTask()
#     # db.session.add(new_project_task)
#     # db.session.commit()

#     return render_template("project_details.html", 
#                            description=task, 
#                            status=status, 
#                            project=project)

    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)