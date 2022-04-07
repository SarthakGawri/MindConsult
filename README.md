# MindConsult
Final Project For [CS50's Web Programming with Python 🐍 and JavaScript](https://cs50.harvard.edu/web)

## About Mindconsult
Mindconsult is a mental health consultation web application made using Django, Django channels, JavaScript, HTML, CSS.

This application contains 2 django apps users and consultation.

Users app handles user registration and authentication for consultants and patients using Django's default authentication system customized according to the project.

Consultation app handles the live chat consultation between patients and consultants using [Django Channels](https://channels.readthedocs.io/en/stable/), Redis and [JavaScript WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket).

## Distinctiveness and Complexity

This project is sufficiently distinct from the other projects in this course and, is not based on the old CS50W Pizza project.

It is neither a social network project nor an e-commerce project. It utilizes Django (with 3 models) and JavaScript.

It is more complex than the other projects as it also uses Django Channels, Redis and Custom Authentication.

Your web application must be mobile-responsive.

## Files

## How to run

To run this project locally, follow these steps

1. Clone this repo or download zip
2. Unzip it
3. In a terminal, navigate to the project directory
4. Run below steps in the project directory

```
python -m venv env or python3 -m venv env

env\Scripts\activate.bat or source env/bin/activate

pip install -r requirements.txt or pip3 install -r requirements.txt

python manage.py runserver or python3 manage.py runserver
```


## Acknowledgements and References
