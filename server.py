from flask import (Flask, render_template, request, redirect, flash, session, jsonify)

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
    work_performed = request.form.get('work_performed') 
    problems_encountered = request.form.get('problems_encountered')
    client_requests = request.form.get('client_requests') 
    project_id = request.form.get('project_id')

    daily_report = crud.create_new_daily_report(employee_id, 
        days_on_site,  work_performed, problems_encountered, client_requests, project_id)
    if daily_report:    
        result_code = 'OK'
        result_text = "Your daily report has been submitted"
    else:
        result_code = 'Error'
        result_text = "Your daily report has not been submitted"
    return jsonify({'code': result_code, 'msg': result_text})
@app.route('/daily_reports/project_id')
def show_daily_report(project_id):
    """Get daily reports by project id."""

    daily_report = crud.get_daily_report_by_id(project_id)

    return render_template('daily_report_details.html', daily_report=daily_report)

@app.route('/projects')     
def get_all_projects():
    """View all projects"""
    
    projects = crud.get_all_projects()

    # print(projects)
    return render_template('all_projects.html', projects=projects)

@app.route('/projects', methods=['POST'])
def create_new_project():
    """Create a new project"""      
     
    project_name = request.form.get('project_name') 
    planned_start_date = request.form.get('planned_start_date') 
    actual_start_date = request.form.get('actual_start_date') 
    actual_end_date = request.form.get('actual_end_date')
    project_description = request.form.get('project_description') 
    project_location = request.form.get('project_location')

    project = crud.create_new_project(project_name, planned_start_date, actual_start_date, 
    actual_end_date, project_description, project_location)
    if project:    
        return render_template("project_added.html",
                        project_id=project_name)
    else:
    # show the form, if it wasn't submitted
        return render_template("homepage.html")
    

@app.route('/login', methods=['POST'])
def user_login():
    """Log an employee into the website"""

    email = request.form.get('email')
    password = request.form.get('password')
    
    employee = crud.check_employee_login_info(email, password)    

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
