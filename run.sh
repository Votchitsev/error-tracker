migrations () {
  python manage.py makemigrations
  python manage.py migrate
}

run () {
  python manage.py runserver 0.0.0.0:8000
}

while true; do
  migrations
  run
  sleep 1
done
