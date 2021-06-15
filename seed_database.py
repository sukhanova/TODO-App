"""Script to seed database."""
from datetime import datetime
from sqlalchemy import func

from model import db, User, Project, Task, connect_to_db
from server import app

import forgery_py

def generate_date():
    return datetime.now()
    

def create_users():
    """Add users to users table."""
    
    print('creating users...')

    nkmishra = User(fname='Neeraj',
                lname='Mishra',
                username='nkmishra',
                email='nkmishra@gmail.com',
                password='nkmishratest')
    
    spanda = User(fname='Subho',
                lname='Panda',
                username='spanda',
                email='spanda@gmail.com',
                password='spandatest')
    
    moyosore = User(fname='Moyo',
                lname='Olomoye',
                username='moyosore',
                email='moyosore@gmail.com',
                password='smoyosoretest')
    
    kberg = User(fname='Kaya',
                lname='Berg',
                username='kberg',
                email='kberg@gmail.com',
                password='kbergtest')
    
    

    db.session.add_all([nkmishra, spanda, moyosore, kberg])
    db.session.commit()


def create_projects():
    """Add projects to projects table."""
    
    print('creating projects...')
    
    
    project1 = Project(title="Role of secretory proteins in tuberculosis pathogenesis.",
                       description="Mtb secrets more than 500 small proteins and peptides which is know as secretome.",
                       start_date="03-12-2021",
                       creator="nkmishra"
                       )
    
    
    project2 = Project(title="Deciphiring the role of homoserine dehydrogenase in methionine biosynthesis.",
                       description="Methionine is an essential amino acid. Methinine biosynthesis pathway is absent in all mammales therefore this pathway can be targeted for next generation antibiotics.",
                       start_date="05-24-2021",
                       creator="nkmishra")
    
    
    project3 = Project(title="Epigenetic makeup of host cells during Mtb infection.",
                       description="Mtb changes epigenetic landscape of infected host cells.",
                       start_date="06-17-2021",
                       creator="kberg")
    
    
    db.session.add_all([project1, project2, project3])
    db.session.commit()
    
    
def create_tasks():
    """Add tasks to tasks table."""
    
    print('creating tasks...')
    
    task1 = Task(description="Grow Mtb in culture at saturation OD.",
                    created_at=generate_date())
    
    task2 = Task(description="Collect the media from Mtb culture filtrate and lyophilize",
                    created_at=generate_date())
    
    task3 = Task(description="Fractionate the lyophylized filtrate accoeding to size, hydrophobic nature of proteins and peptides",
                    created_at=generate_date())
    
    task4 = Task(description="Do mass spectrometry and identify the proteins and peptide sequence",
                    created_at=generate_date())
    
    task5 = Task(description="Define most abundant protein or peptide followed by its expression/synthesis",
                    created_at=generate_date())
    
    task6 = Task(description="Add the synthesized peptide/protein to macrophagre cell culture and study cell phenotype",
                    created_at=generate_date())
    
    task7 = Task(description="Collect the macrophages for different period of time after trearment by protein/peptide",
                    created_at=generate_date())
    
    task8 = Task(description="Fractionate cells and collect cytosolic proteins, nucleus and membranes",
                    created_at=generate_date())

    
    db.session.add_all([task1, task2, task3, task4, task5, task6, task7, task8])
    db.session.commit()   

        
if __name__ == "__main__":
    from flask import Flask
    connect_to_db(app)
    db.drop_all()
    db.create_all()
    

    create_users()
    create_projects()
    create_tasks()
    
    db.session.commit()