from flask import (render_template, redirect, url_for, request)
from models import db, Project, app
from datetime import datetime



# root page/homepage
@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)



# route - for looking details of a project
@app.route("/project/<id>")
def project(id):
    project = Project.query.get(id)
    return render_template("detail.html", project=project)



# route - for adding a new project
@app.route("/project/new", methods=['GET', 'POST'])
def project_new():
    if request.form:
        #print(request.form)
        #print(request.form['name'])
        # create the Python object
        new_project = Project(title= request.form['Title'],
                            date_finished = datetime.strptime(request.form['Date finished'], '%Y-%m-%d'),
                            description=request.form['Description'],
                            skills_practiced=request.form['Skills practiced'],
                            github_link= request.form['Github Link'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))                         
    return render_template('projectform.html', project=None)



# route for editing a project
@app.route("/project/<id>/edit", methods=['GET', 'POST'])
def project_id_edit(id):
    project = Project.query.get(id)
    if request.form:
        project.title= request.form['Title']
        project.date_finished = datetime.strptime(request.form['Date finished'], '%Y-%m-%d')
        project.description=request.form['Description']
        project.skills_practiced=request.form['Skills practiced']
        project.github_link= request.form['Github Link']
        return redirect(url_for('index'))
    return render_template('editproject.html',project=project)


#### MISSING TEMPLATE "editproject.html"

# route for deleting a project
@app.route("/project/<id>/delete")
def project_id_delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

### NOT SURE IF I AM MISSING SOMETHING HERE ABOVE



project1 = Project(title='Number guessing game',
                   date_finished = datetime(2024,4,22), #'2024-April-22'
                   description='A console game consisting in guessing a random number, wich tells you how close you are getting to the number.',
                   skills_practiced='Creating and using  functions. Lists. The Random library. While Loops. For Loops. Exceptions. If statements.',
                   github_link='https://github.com/Gus7510/Treehouse-Techdegree-Unit-1')

project2 = Project(title='Basketball Stats Tool',
                   date_finished = datetime(2024,5,10), #'2024-May-10'
                   description='A console-based basketball team statistics tool.',
                   skills_practiced='Tuples. Functions packing and unpacking. Dictionaries. Sets.',
                   github_link='https://github.com/Gus7510/Treehouse-Techdegree-Unit-2')

project3 = Project(title='Phrase Hunters',
                   date_finished = datetime(2024,6,20), #'2024-June-20'
                   description='A word guessing game built using Object-Oriented Programing.',
                   skills_practiced='Object Oriented Programming. Dunder Main.',
                   github_link='https://github.com/Gus7510/Treehouse-Techdegree-Unit-3')

project4 = Project(title='Store Inventory with SQLAlchemy',
                   date_finished = datetime(2024,8,2), # '2024-August-2'
                   description='A console application that loads an existing stores inventory data from a CSV file into a SQLite database.',
                   skills_practiced='SQLAlchemy. CSV File import and export.',
                   github_link='https://github.com/Gus7510/Treehouse-Techdegree-Unit-4')



if __name__== "__main__":
    with app.app_context():
        db.create_all()
        #db.session.add_all([project1, project2, project3, project4])
        #db.session.commit()
        # the database has already been created.
    app.run(debug=True, port=8000, host="127.0.0.1")



