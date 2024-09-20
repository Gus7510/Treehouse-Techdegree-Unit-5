from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date_finished = db.Column('Date finished', db.DateTime, default=datetime.datetime.now)
    description = db.Column('Description', db.Text)
    skills_practiced = db.Column('Skills practiced', db.Text)
    github_link = db.Column('Github Link', db.Text)

    def __repr__(self):
        return f"""<Project (Title: {self.title})
        Date of creation: {self.date_finished}
        Skills practiced: {self.skills_practiced}
        Description: {self.description}
        Github Link: {self.github_link}"""








