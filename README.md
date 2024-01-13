# Error Tracker

Error Tracker - сервис для сбора и хранения информации об ошибках во фронтенд и бекенд приложениях.


## Быстрый запуск 

Для запуска приложения необходимо выполнить следующие шаги...

### Клонирование репозитория

```
git clone https://github.com/Votchitsev/error-tracker.git
```

### Создание .env файла

```
# App config
SECRET_KEY=str # секретный ключ приложения
DEBUG=bool # включение режима отладки

# Database config
DB_NAME=str # название базы данных
DB_USER=str # имя пользователя базы данных
DB_PASSWORD=str # пароль пользователя базы данных
DB_HOST=str # хост базы данных
DB_PORT=str # порт базы данных
```

### Запуск приложения
```
# запуск в режиме отладки
make dev

# запуск в режиме публикации
make build
```