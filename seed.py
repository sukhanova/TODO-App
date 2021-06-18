import datetime
from sqlalchemy import func

from model import User, Project, Task, ProjectTask, UserTask, UserProject, connect_to_db, db
from server import app

def create_users():
    """Add users to users table."""
    
    print("users")
    
    neeraj = User(fname="Neeraj",
                  lname="Mishra", 
                  username="nkmishra",
                  email="nkmishra@gmail.com",
                  password="nkmishratest")
    
    
    subho = User(fname="Subho",
                 lname="Panda",
                 username="spanda",
                 email="spanda@gmail.com",
                 password="spandatest")


    moyo = User(fname="Moyo",
                lname="Olomoye",
                username="moyosore",
                email="moyosore@gmail.com",
                password="smoyosoretest")
    
    kaya = User(fname="Kaya",
                lname="Berg",
                username="kberg",
                email="kberg@gmail.com",
                password="kbergtest")


    db.session.add_all([neeraj, subho, moyo, kaya])
    db.session.commit()
    

def create_projects():
    """Add projects to projects table."""
    
    print("projects")
    
    project1 = Project(title="Role of secretory proteins in tuberculosis pathogenesis.",
                       description="Mtb secrets more than 500 small proteins and peptides which is know as secretome.",
                       start_date="2021-03-12",
                       creator="nkmishra")
    
    project2 = Project(title="Deciphiring the role of homoserine dehydrogenase in methionine biosynthesis.",
                       description="Methionine is an essential amino acid. Methinine biosynthesis pathway is absent in all mammales therefore this pathway can be targeted for next generation antibiotics.",
                       start_date="2021-05-24",
                       creator="nkmishra")
    
    project3 = Project(title="Epigenetic makeup of host cells during Mtb infection.",
                       description="Mtb changes epigenetic landscape of infected host cells.",
                       start_date="2021-06-16",
                       creator="kberg")
    
    
    db.session.add_all([project1, project2, project3])
    db.session.commit()
    
    
def create_tasks():
    """Add tasks to tasks table."""
    
    print("tasks")
    
    task1 = Task(description="Grow Mtb in culture at saturation OD.",
                 done=False)
    
    task2 = Task(description="Collect the media from Mtb culture filtrate and lyophilize.",
                 done=True)
    
    task3 = Task(description="Do mass spectrometry and identify the proteins and peptide sequence.",
                 done=False)
    
    task4 = Task(description="Define most abundant protein or peptide followed by its expression/synthesis.",
                 done=False)
    
    task5 = Task(description="Add the synthesized peptide/protein to macrophagre cell culture and study cell phenotype.",
                 done=False)
    
    task6 = Task(description="Collect the macrophages for different period of time after trearment by protein/peptide.",
                 done=True)
    
    task7 = Task(description="Fractionate cells and collect cytosolic proteins, nucleus and membranes",
                 done=False)
    
    task8 = Task(description="Prepare DNA and RNA samples from treated cells and study the base modifications by massspectrometery.",
                 done=False)

    task9 = Task(description="Perform RNAseq and find out the changes in trnscription after macrophages treatment by peptide/protein.",
                 done=False)


    db.session.add_all([task1, task2, task3, task4, task5, task6, task7, task8, task9])
    db.session.commit()
    
    
    
def create_project_tasks():
    """Add project tasks to project_tasks table."""
    
    print("project_tasks")
    
    projectTask1 = ProjectTask(task_id=1, project_id=1)
    projectTask2 = ProjectTask(task_id=2, project_id=1)
    projectTask3 = ProjectTask(task_id=3, project_id=1)
    projectTask4 = ProjectTask(task_id=4, project_id=1)
    projectTask5 = ProjectTask(task_id=5, project_id=1)
    projectTask6 = ProjectTask(task_id=1, project_id=2)
    projectTask7 = ProjectTask(task_id=6, project_id=2)
    projectTask8 = ProjectTask(task_id=7, project_id=2)
    projectTask9 = ProjectTask(task_id=8, project_id=2)
    projectTask10 = ProjectTask(task_id=1, project_id=3)
    
    
    db.session.add_all([projectTask1, projectTask2, projectTask3, projectTask4, projectTask5, projectTask6, projectTask7, projectTask8, projectTask9, projectTask10])
    db.session.commit()
    
    
 
def create_users_projects():
    """Add users and project to users_projects table."""
    print("users_projects")
    
    user_project1 = UserProject(user_id=1, project_id=1)
    user_project2 = UserProject(user_id=1, project_id=2)
    user_project3 = UserProject(user_id=2, project_id=2)
    user_project4 = UserProject(user_id=3, project_id=2)
    user_project5 = UserProject(user_id=4, project_id=3)
    
    db.session.add_all([user_project1, user_project2, user_project3, user_project4, user_project5])
    db.session.commit()
    

def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    #Get max user_id in the database:
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    #Set new value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()   
    
    
if __name__ == "__main__":
    from flask import Flask
    connect_to_db(app)
    db.drop_all()
    db.create_all()
   
    # call your functions above
    create_users()
    create_projects()
    create_tasks()
    create_project_tasks()
    create_users_projects()
    
    
    db.session.commit()
