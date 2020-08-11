

1. create virtualenv and clone this project

2. create settings_local.py using settings_local.py.example

3. set up external_apps directory and clone user_manager

4. install required libraries

pip install -r requirements.txt

5. create database migrations for user manager

python manage.py makemigrations user_mananger

6. set up the sqlite3 database

python manage.py migrate
python manage.py createsuperuser





