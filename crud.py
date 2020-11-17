"""CRUD operations."""

from model import db, Employee, Project, DailyReport, connect_to_db


def check_employee_login_info(email, password):
    """check if the users email and password match in the database"""

    return Employee.query.filter((Employee.email == email) & (Employee.password == password)).first()

def get_all_employees():
    return Employee.query.all()
    
def get_all_projects():
    return Project.query.all()

def get_all_daily_reports():
    return DailyReport.query.all()

def create_new_daily_report(employee_id, days_on_site, work_performed, problems_encountered, 
    client_requests, project_id):
    """Create a new daily report and print a confirmation."""

    daily_reports = DailyReport(employee_id=employee_id, 
                                days_on_site=days_on_site, 
                                work_performed=work_performed, 
                                problems_encountered=problems_encountered,
                                client_requests=client_requests,
                                project_id=project_id)

    db.session.add(daily_reports)
    db.session.commit()

    return daily_reports



if __name__ == '__main__':
    from server import app
    connect_to_db(app)