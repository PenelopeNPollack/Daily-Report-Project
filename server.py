from flask import (Flask, render_template, request, redirect, flash, session)

# from model import connect_to_db
import crud
from model import connect_to_db
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "secret"

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """View home page"""
    
    return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def user_login():
    """Log a user into the website"""

    email = request.form.get('email')
    password = request.form.get('password')
    print(email, password)
    user = crud.check_user_login_info(email, password)
    print(user)

    if user:
        flash("Successful login")
    else:
        flash("Login info incorrect, please try again")
        return redirect('/')

    employees=crud.get_all_employees()
    projects=crud.get_all_projects()
    return render_template('create_daily_report.html', projects=projects, employees=employees)

  

if __name__ == '__main__':
    crud.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
    