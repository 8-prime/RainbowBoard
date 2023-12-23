# RainbowBoard

An app that loads data from [Schwarzes Brett](https://schwarzesbrett.bremen.de/)



## Project Technology

The project leverages the Django framework to build serve the data, which is stored in a PostgrSQL DB.
Leveragin the RSS-Feed supplied from the Schwarzes Brett in conjunctuon with web scraping lays the foundation for the data that will later be served


## Project setup

Here the different steps to initially setup the project will be shown.
One important note is that this project will be run using Docker Compose.

### Databas
The PostgrSQL DB will be hosted using the default docker image with some basic settings

### Django Setup

First to use Django in conjuction with PostgrSQL we have to install a pip Package `pip install psycopg2-binary
`

Then the Django project has to be initiated `django-admin startproject RainbowBoard .`
The dot at the end is relevant as we are already in a folder called RainbowBoard for the git repo.

The databases object in the *settings.py* has to be extended for our db instance

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'NAME': 'db',
        'PASSWORD': '*******',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

Next the application for our project has to be created as part of the Django project. 
For this we use `python manage.py startapp apartments`
In this app inside the *models.py* we add our model. This is nothing special. Just go check yourself :D.

Then we extend the *settings.py* installed apps with the app we created before

```
INSTALLED_APPS = [
    ...
    'apartments',
]
```

After this the basic setup is done and we get to migrations.
To create a migration for our model we run `python manage.py makemigrations apartments`
Then we can run `python manage.py migrate` 



python manage.py makemigrations rentals

python manage.py migrate
