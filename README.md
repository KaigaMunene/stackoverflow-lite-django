# stackoverflow-lite-django

A django APi for users to ask questions and give answers to asked questions.

## Implemented Features
* Users can create an account and login.
* Authenticated users can post questions.
* Authenticated users can update their questions.
* Authenticated users can delete their questions.
* Authenticated Users can post answers to questions.
* Users can view various questions and answers to questions.

## Extra Feature
* Users can search for questions on the platform.

## Technologies Used
* [Django](https://www.djangoproject.com/) - python webframework.
* [Django-rest-framework](https://www.django-rest-framework.org/) - powerful and flexible toolkit for building Web APIs.
* [simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) - A JSON Web Token authentication plugin for the Django REST Framework.
* [PostgreSQL](https://www.postgresql.org) - Object relational database.
* [pgAdmin](https://www.pgadmin.org/) - Open Source administration and development platform for PostgreSQL.
* [Black](https://black.readthedocs.io/en/stable/) - python code formatter.
* [isort](https://pypi.org/project/isort/) - a Python utility / library to sort Python imports.

### Installation
```
    $ git clone git@github.com:KaigaMunene/stackoverflow-lite-django.git
    $ cd stackoverflow-lite-django
    $ sudo apt install pipenv (https://pipenv.pypa.io/en/latest/install/#installing-pipenv) ensure you have python and pip installed
    $ pip install -r requirements.txt 
    $ pipenv install (you should be able to install the files in the requirements.txt) 
```

## Running the application
open .env file and copy your postgres database url
```
    #.env file
    DATABASE_URL=postgres://username:password@hostname/databasename
    
    $ python manage.py runserver
```

## Testing
Requirements
* [Postman](https://www.getpostman.com/) - API development and testing environment.

* or through [Heroku](https://django-stackoverflow-lite.herokuapp.com/) - just click the link

Testing with Postman
* Install Postman by following the link above.
* Navigate to `http://127.0.0.1:8000/` in Postman to access the application.
* The endpoints are down below

### Endpoints
#### Users Endpoints
Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/users/register/` | Add a user
POST | `/api/v1/users/token/` | Login a user

#### Questions Endpoints (you must be a logged in user)

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/qs/` | Add a question
GET | `/api/v1/qs/questions` | Lists all questions
GET | `/api/v1/qs/questions?title={search_string}` | Search a questions
GET | `/api/v1/qs/question/{question_id}` | Retrieve one question
PUT | `/api/v1/qs/question/{question_id}` | Edit a question of a logged in user
DELETE | `/api/v1/qs/question/{question_id}` | Delete a request of a logged in user

#### Answers Endpoints (you must be a logged in user)
Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/ans/answer/` | Add an answer
GET | `/api/v1/ans/answers/` | Lists all answers
GET | `api/v1/ans/answers/question/` | retrieve  all answers for a certain question
PUT | `/api/v1/ans/answer/{answerID}` | Edit an answer
DELETE | `/api/v1/ans/answer/{answerID}` | Delete an answer

## Credits
This challenge was part of cycle 2 trainning in SkaeHub Techlologies.
