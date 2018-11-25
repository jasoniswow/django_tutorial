The tutorial of Django

Basic flow:
user request in browser -> url -> view -> HTML templates -> view -> user browser
The urls.py links to stuff in views.py based on the requested url
The views.py controls the high level template and data to use
The html template defined all the webpage showing details

Each project contains several apps, each app has it's own urls.py, views.py and templates
Create a project: python manage.py startproject $NAME
Create an app: python manage.py startapp $NAME

Each type of data is called a model, defined as a class
The model needs to be migrated to the database as a single table (in "db.sqlite3")
Make migration and then migrate the model:
"python manage.py makemigrations"
"python manage.py migrate"
Each time the model changes, re-do the above two steps

Create super user login: "python manage.py createsuperuser"
Register your models to admin area so that you can add/delete... models as admin through webpage

Django does handle static files (images, javascript, ...) very well, that's usually done through AWS
Define the static file path in settings.py (assets/...)
Use the static files in the html templates

In order for the django webpage public, run:
sudo npm install -g localtunnel
lt --port 8000 --subdomain jasoniswow
