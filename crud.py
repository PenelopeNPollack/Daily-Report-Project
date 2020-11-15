"""CRUD operations."""

from model import db, Employee, Project, connect_to_db


def check_user_login_info(email, password):
    """check if the users email and password match in the database"""

    return Employee.query.filter((Employee.email == email) & (Employee.password == password)).first()

def get_all_employees():
    return Employee.query.all()
    
# def get_all_projects():
#     return Project.query.all()
    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)