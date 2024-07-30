# Celery Project 
Project built using django, redis, and celery

### Requirements:
* Python 3.10.12
* Django 5.0.7
* redis 5.0.7 
* celery 5.4.0

### Steps to run this project:
1. Create virtual environment using python -m venv 'celeryvenv' command. 
2. Activate virtual environment using source 'celeryvenv/bin/activate' command.
3. Install django, redis and celery using pip command.
4. Install requirements using pip install -r requirements.txt command. 
5. Create django project and application.
6. Create celery.py file inside inner project folder to write basic config code. 
7. Configure django celery in settings.py file.
8. Create tasks.py file inside django application to write tasks.
9. Mention task inside views.py file to trigger celery task.
10. Run python manage.py migrate command to create database table. 
11. Create superuser using python manage.py createsuperuser command. 
12. For periodic task execution install django-celery-results using pip install django-celery-results command. 
13. Run server using python manage.py runserver command.
14. Start celery beat using celery -A celeryproject beat -l info command. 
15. Start celery worker using celery -A celeryproject worker -l INFO command.
