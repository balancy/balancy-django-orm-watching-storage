# Django-ORM-Watching-Storage

App allows you to imitate storage monitoring system. You can see all passcards info, monitor visits journal and which passcards are active at the moment.

### How to install

Python3 and Git should be already installed. 

1. Clone the repository by command:
```console
git clone https://github.com/balancy/balancy-django-orm-watching-storage
```
2. Inside cloned repository create virtual environment by command:
```console
python -m venv env
```
3. Activate virtual environment. For linux-based OS:
```console
source env/bin/activate
```
For Windows:
```console
env\scripts\activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Rename file `.env.example` to `.env` and initialize your propre variables to initialize a database
```console
ALLOWED_HOSTS = 127.0.0.1,localhost,your_database_host
DEBUG = True
ENGINE = 'django.db.backends.postgresql_psycopg2'
HOST = your_database_host
NAME = your_database_name
PASSWORD = your_database_password
PORT = your_database_port
USER = your_database_user
```
Those environmental variables are necessary for correct work of application. Some variables are already initialized by default. 

6. Run the script by command:
```console
python manage.py runserver
```
The app will be accessible via link `http://127.0.0.1:8000/` 

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
