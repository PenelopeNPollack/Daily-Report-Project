# Hackbright Academy Capstone Project

## Hackbright Academy Full-Stack Software Engineering Program

This web app replaces a construction project daily progress report word document and saves the data directly into a PostgreSQL database.

### Technologies:

* Python
* PostgreSQL
* SQLAlchemy
* HTML
* jQuery
* Jinja
* Javascript (AJAX)
* CSS
* Bootstrap
* Git

### MVP
* Employee can log in
* Employee can create a new daily report and save it
* Employee can view all saved daily reports

### 2.0
* Form updates days on site
* Employee can view saved daily reports by daily report id or by project
* Added log out feature


### Future Implementations
* Automate work flows so that the submission of one form triggers another form to be sent
* Ability to add photos either directly or via dropbox
* Send forms with pre-populated data to notify employees about project information

## Requirements
* PostgreSQL
* Python 3.7.3

You are welcome to run this app locally on your own computer. To do so, first clone this repository:

```shell
$ git clone https://github.com/PenelopeNPollack/Daily-Report-Project.git
```

Create and activate a virtual environment:

```shell
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```

Install dependencies:

```shell
(env) $ pip3 install -r requirements.txt
```

Create a secrets.sh file and save your secret key for this app using the following syntax:

```
export SECRET_KEY="your_secret_key"
```

Activate the secrets.sh file in your terminal:

```shell
(env) $ source secrets.sh
```

Create the database:

```shell
(env) $ createdb project
```

Start the backend server:

```shell
(env) $ python3 server.py
```

Open a new window and visit this address: http://0.0.0.0:5000/ to view the Create A Daily Report app.
