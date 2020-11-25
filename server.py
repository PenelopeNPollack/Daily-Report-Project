from flask import (Flask, render_template, request, redirect, flash, session, jsonify)

# from model import connect_to_db
import crud
from model import connect_to_db
from jinja2 import StrictUndefined

app = Flask(__name__)
# A secret key needed to use Flask sessioning features
app.secret_key = "secret"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """View homepage"""
    
    return render_template("homepage.html")

@app.route('/days_on_site')
def days_on_site():
    """Return the number of days on a project site"""

    return 
    
@app.route('/daily_report', methods=['POST'])
def create_new_daily_reports():
    """Create a new daily reports"""

    employee_id = request.form.get('employee_id')
    employee_name=request.form.get('employee_name') 
    work_performed = request.form.get('work_performed') 
    problems_encountered = request.form.get('problems_encountered')
    client_requests = request.form.get('client_requests') 
    project_id = request.form.get('project_id')

    daily_report = crud.create_new_daily_report(employee_id, 
        employee_name,  work_performed, problems_encountered, client_requests, project_id)
    if daily_report:          
        result_text = "Your daily report has been submitted"
    else:        
        result_text = "Your daily report has not been submitted"
    return jsonify({'msg': result_text})
    
@app.route('/daily_reports/<project_id>')
def show_daily_reports(project_id):
    """Get daily reports by project id."""
    daily_reports = crud.get_all_daily_reports_by_project(project_id)

    return render_template('daily_reports_by_project_id.html', daily_reports=daily_reports)

@app.route('/daily_reports')     
def get_all_daily_reports():
    """View all daily reports"""
    
    daily_reports = crud.get_all_daily_reports()

    return render_template('all_daily_reports.html', daily_reports=daily_reports)

@app.route('/daily_report/<daily_report_id>')
def get_daily_report_by_id(daily_report_id):

    daily_report = crud. get_daily_report_by_id(daily_report_id)

    print(daily_report)
    return render_template('daily_report_details.html', daily_report=daily_report)

@app.route('/projects')     
def get_all_projects():
    """View all projects"""
    
    projects = crud.get_all_projects()

    return render_template('all_projects.html', projects=projects)

@app.route('/project', methods=['POST'])
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
        return render_template("all_projects.html",
                        project_id=project_name)
    else:
    # show a message that the form wasn't submitted
        result_text = "Your daily report has not been submitted"
    return jsonify({'msg': result_text})

@app.route('/return_count/<project_id>')
def return_days_on_site_count(project_id):
    count = crud.get_count_of_daily_reports_by_project(project_id)
    return str(count)
    

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
        # days_on_site=crud.get_all_daily_reports_by_project()
        return render_template('create_daily_report.html', projects=projects, employees=employees)
    else:
        flash("Login info incorrect, please try again")
        return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == '__main__':
    crud.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
