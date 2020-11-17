from flask import (Flask, render_template, request, redirect, flash, session)

# from model import connect_to_db
import crud
from model import connect_to_db
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "secret"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """View homepage"""
    
    return render_template("homepage.html")

@app.route('/daily_report')     
def view_all_daily_reports():
    """View all daily reports"""
    
    daily_reports = crud.get_all_daily_reports()

    # print(daily_reports)
    return render_template('all_daily_reports.html', daily_reports=daily_reports)

@app.route('/daily_report', methods=['POST'])
def create_new_daily_reports():
    """Create a new daily reports"""

    employee_id = request.form.get('employee_id') 
    days_on_site = request.form.get('days_on_site') 
    worked_performed = request.form.get('work_performed') 
    problems_encountered = request.form.get('problems_encountered')
    client_requests = request.form.get('client_requests') 
    project_id = request.form.get('project_id')

    daily_report = crud.create_new_daily_report(employee_id, 
        days_on_site,  worked_performed, problems_encountered, client_requests, project_id)
    if daily_report:    
        return render_template("daily_report_added.html",
                        daily_report_id=project_id)
    else:
    # show the form, if it wasn't submitted
        return render_template("homepage.html")

@app.route('/project')     
def view_all_projects():
    """View all projects"""
    
    projects = crud.get_all_projects()

    # print(projects)
    return render_template('all_projects.html', projects=projects)

# @app.route('/daily_report', methods=['POST'])
# def create_new_daily_reports():
#     """Create a new daily reports"""

#     employee_id = request.form.get('employee_id') 
#     days_on_site = request.form.get('days_on_site') 
#     worked_performed = request.form.get('work_performed') 
#     problems_encountered = request.form.get('problems_encountered')
#     client_requests = request.form.get('client_requests') 
#     project_id = request.form.get('project_id')

#     daily_report = crud.create_new_daily_report(employee_id, 
#         days_on_site,  worked_performed, problems_encountered, client_requests, project_id)
#     if daily_report:    
#         return render_template("daily_report_added.html",
#                         daily_report_id=project_id)
#     else:
#     # show the form, if it wasn't submitted
#         return render_template("homepage.html")
    

@app.route('/login', methods=['POST'])
def user_login():
    """Log an employee into the website"""

    email = request.form.get('email')
    password = request.form.get('password')
    
    employee = crud.check_employee_login_info(email, password)    

    # if "employee_id" not in session:
    #     session["employee_id"] = employee.employee_id
    # else:
    #     active_employee = session.get("employee_id")

    """Check to see if user login is sucessful"""
    if employee:
        flash("Successful login")
        employees=crud.get_all_employees()
        projects=crud.get_all_projects()
        return render_template('create_daily_report.html', projects=projects, employees=employees)
    else:
        flash("Login info incorrect, please try again")
        return redirect('/')


if __name__ == '__main__':
    crud.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
