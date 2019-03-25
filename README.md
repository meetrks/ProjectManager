Project Manager

Installation Guide

Pre Requirements-
- Python 3.x
- virtualenv

Create virtual environment and install dependencies-

virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

You can run server using-

python manage.py runserver


Open <http://127.0.0.1:8000> in browser!

Users:
Admin (Can view, edit, delete projects/tasks):
    username: admin
    password: admin

General User (Can view the projects/tasks):
    username: user
    password: user@123


