migrations () {
  python manage.py makemigrations
  python manage.py migrate
}

run () {
  python manage.py runserver 127.0.0.1:8000
}

while true; do
  migrations
  run
  sleep 1
done
