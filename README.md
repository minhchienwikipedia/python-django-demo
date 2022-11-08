### Learning Python - Django

#### How to run?
1. Start server:
```sh
python manage.py runserver
```
2. Login admin page: http://127.0.0.1:8000/admin
3. Check the main page: http://127.0.0.1:8000/home

#### How to edit?
##### To update the model (table in database):
1. Go to [models.py](./home/models.py) of the app (this example is `home`) and create new class or update class fields
2. [Update](#update-to-database)
#### Create new app:
1. Run this command
```sh
python manage.py startapp {{app_name}} 
```
2. Go to [settings.py](./todo/settings.py) and add name of app config to INSTALLED_APPS
Example new app is demo: `demo.apps.DemoConfig` (or go to [apps.py](./home/apps.py) to check the name)
3. [Update](#update-to-database)

##### Update to database
```sh
python manage.py makemigrations
python manage.py migrate   
```
