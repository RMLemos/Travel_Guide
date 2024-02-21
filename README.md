## Travel Guide API
Getting Started with Django REST Framework

This repository is intended to serve as a tool for creating other API.

### Usage

1. After cloning this repository, create a virtual environment and install the requirements listed in the 'requirements.txt' file:

```
pip install -r requirements.txt
```

2. In the file setting.py, configure the database settings.
3. Execute below commands:

```
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser for admin access and follow instructions:

```
python manage.py createsuperuser
```

5. Running the tests

```
python manage.py runserver
```

### Tools
+ Django
+ Laragon
+ MySQL
+ Python

### Reference:
+ https://www.udemy.com/course/apis-restful-com-django-rest-framework/