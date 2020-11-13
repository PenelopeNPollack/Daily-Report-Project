"""A web application for tracking employees, projects, and daily reports."""

from datetime import datetime

from flask import Flask, render_template, request
from model import connect_to_db, db, Employee, Project

app = Flask(__name__)


def index():
    """Return homepage."""

    return "homepage.html"

@app.route("/login")
def login_page():
    """Login a user"""

    session['user_id'] = 
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.check_user_login_info(email, password)

    if "user_id" not in session:
        session["user_id"] = user.user_id
    else:
        active_user = session.get("user_id")

    if user:
        flash("Successful login")
    else:
        flash("Login info incorrect, please try again")
    
    
    return redirect('/create_daily_report_form.html')


@app.route("/create_daily_report")
def create_project():
    """Display form to create a daily report."""

    projects = Project.query.all()

    return render_template("create_daily_report_form.html", projects=projects)


@app.route("/daily_reports", methods=["POST"])
def create_new_daily_report():
    project_name = request.form.get("project_name")
    employee_id = request.form.get("employee_id")

    new_project = Project(project_name=project_name, planned_start_date=datetime.now())
    employee = Employee.query.get(employee_id)

    new_project.employees.append(employee)
    db.session.add(new_project)
    db.session.commit()

    return "You did it!"


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
