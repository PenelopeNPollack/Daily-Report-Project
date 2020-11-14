"""Data model for daily reports."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


# ---------------------------------------------------------------------#


class Employee(db.Model):
    """An Employee."""

    __tablename__ = "employees"

    employee_id = db.Column(
        db.Integer, autoincrement=True, unique=True, primary_key=True
    )
    full_name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String)

    projects = db.relationship(
        "Project", secondary="projects_employees", backref="employees"
    )

    def __repr__(self):
        """Clear representation of an employee."""

        repr_str = "<Employee employee_id={employee_id}>"

        return repr_str.format(employee_id=self.employee_id)


class Project(db.Model):
    """A project."""

    __tablename__ = "projects"

    project_id = db.Column(
        db.Integer, autoincrement=True, unique=True, primary_key=True
    )
    project_name = db.Column(db.String, unique=True, nullable=False)
    planned_start_date = db.Column(db.DateTime, nullable=False)
    actual_start_date = db.Column(db.DateTime)
    actual_end_date = db.Column(db.DateTime)
    project_description = db.Column(db.String)
    project_location = db.Column(db.String)

    def __repr__(self):
        """Clear representation of a project."""

        repr_str = "<Project project_id={project_id}>"

        return repr_str.format(project_id=self.project_id)


class ProjectsEmployees(db.Model):
    """A bridge table"""

    __tablename__ = "projects_employees"

    projects_employees_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(
        db.Integer, db.ForeignKey("projects.project_id"), nullable=False
    )
    employees_id = db.Column(
        db.Integer, db.ForeignKey("employees.employee_id"), nullable=False
    )


class DailyReport(db.Model):
    """A Daily Report."""

    __tablename__ = "daily_reports"

    daily_report_id = db.Column(
        db.Integer, autoincrement=True, unique=True, primary_key=True
    )
    days_on_site = db.Column(db.Integer)
    worked_performed = db.Column(db.Text)
    problems_encountered = db.Column(db.Text)

    project_id = db.Column(
        db.Integer, db.ForeignKey("projects.project_id"), nullable=False
    )
    project = db.relationship("Project", backref="reports")

    def __repr__(self):
        repr_str = "<Daily_Reports daily_report_id={daily_report_id}>"

        return repr_str.format(daily_report_id=self.daily_report_id)


# ---------------------------------------------------------------------#


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///project"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    connect_to_db(app)
    print("Connected to DB.")
