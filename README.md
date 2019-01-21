Features
========
1. Ready-to-go django blog


Environment setup
=================

1 . Starting our Django project
 ```
django-admin startproject "NAME"
```

2 . Creating virtualenv
 ```
virtualenv venv
```

3 . Starting our virtual environment
 ```
source venv/bin/activate
```

4 . Installing + Cloning Git repository
 ```
pip3 install django
```

5 . Migrate
 ```
python3 manage.py migrate
```

5 . Creating superuser
 ```
python3 manage.py createsuperuser
```

 ```
name : admin
password : juro000
```

Settings setup
=================
1 . Creating app inside our project directory
 ```
python3 manage.py startapp accounts
```

2 . Adding our app to settings.py
 ```
INSTALLED_APPS = [
'accounts',
]
```
