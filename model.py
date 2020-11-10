"""Data model for daily reports."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


#---------------------------------------------------------------------#
"""A bridge table"""
projects_employees = db.Table('projects_employees',
    db.Column('project_id', db.Integer, db.ForeignKey('Projects.project_id'), primary_key=True),
    db.Column('employee_id', db.Integer, db.ForeignKey('Employees.employee_id'), primary_key=True)
)

class Employees(db.Model):
    """An Employee."""

    __tablename__ = "employees"

    employee_id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    full_name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False) 
    user_id = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)   
    role = db.Column(db.String)

    projects_employees = db.relationship('Projects', secondary=projects_employees, lazy='subquery',
        backref=db.backref('Employees', lazy=True))

    def __init__(self,
                 employee_id,
                 full_name,
                 email,
                 user_id,
                 password,
                 role):

        """Create an employee."""

        self.employee_id = employee_id
        self.full_name = full_name
        self.email = email  
        self.user_id = user_id
        self.password = password
        self.role = role

    def __repr__(self):
        """Clear representation of an employee."""

        repr_str = "<Employees employee_id={employee_id}>"

        return repr_str.format(employee_id=self.employee_id)

class Projects(db.Model):
    """A project."""

    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    project_name = db.Column(db.String, unique=True, nullable=False)
    planned_start_date = db.Column(db.DateTime, nullable=False)
    actual_start_date = db.Column(db.DateTime)
    actual_end_date = db.Column(db.DateTime)
    project_description = db.Column(db.String)
    project_location = db.Column(db.String)
    daily_reports = db.Column(db.Integer)

    def __init__(self,
                 project_id,
                 project_name,
                 planned_start_date,
                 actual_start_date,
                 actual_end_date,
                 project_description,
                 project_location,
                 daily_reports):
                     
        """Create a project."""

        self.project_id = project_id
        self.project_name = project_name
        self.planned_start_date = planned_start_date 
        self.actual_start_date = actual_start_date
        self.actual_end_date = actual_end_date
        self.project_description = project_description
        self.project_location = project_location
        self.daily_reports = daily_reports

    def __repr__(self):
        """Clear representation of a project."""

        repr_str = "<Projects project_id={project_id}>"

        return repr_str.format(project_id=self.project_id)


class Daily_Reports(db.Model):
    """A Daily Report."""

    __tablename__ = "daily_reports"

    daily_report_id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    daily_report_name = db.Column(db.String, unique=True, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('Projects.project_id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('Employees.employee_id'))
    created_at = db.Column(db.DateTime)
    
    project = db.relationship('Projects', backref='daily_report')
    employee = db.relationship('Employees', backref='daily_report')

    def __init__(self,
                 daily_report_id,
                 daily_report_name,
                 instructions,
                 project_id,
                 employee_id,
                 created_at):

        """Create a daily report."""

        self.daily_report_id = daily_report_id
        self.daily_report_name = daily_report_name
        self.instructions = instructions  
        self.project_id = project_id
        self.employee_id = employee_id
        self.created_at = created_at
        
    def __repr__(self):
        """Clear representation of daily reports."""

        repr_str = "<Daily_Reports daily_report_id={daily_report_id}>"

        return repr_str.format(daily_report_id=self.daily_report_id)

    
#---------------------------------------------------------------------#

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    connect_to_db(app)
    print("Connected to DB.")

    handle_input()

    # To be tidy, we'll close our database connection -- though, since this
    # is where our program ends, we'd quit anyway.

    db.session.close()
