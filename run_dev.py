import os


def run():
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')
    os.system('python manage.py runserver 127.0.0.1:8000')

run()
