# Перед началом работы:

Cоздайте свой **SECRET_KEY** для файла _.env.prod_

**_Windows:_**
```
from secrets import token_bytes
from base64 import b64encode
print(b64encode(token_bytes(32)).decode())
```
**_Linux/MacOs:_**
```
openssl rand -base64 32
```

# Сервис авторизации для InstallBiz.

1. `make start` - Формирование Docker - образа + запуск.
2. `make stop` - Остановка.
3. `make venv` - Создание виртуального окружения
4. `source venv/bin/activate` - Активация виртуального окружения
5. `make install` - Установка зависимостей проекта.
6. `make test` - Тестирование проекта.


## [Документация](http://localhost:8000/docs)

**_В проекте настроены метрики с использованием Grafana + Prometheus.\
Так же настроены продуктовые метрики отвечающие за количество успешных и неуспещных попыток аутентификации._**

# Регистрация и Авторизация

## 1. Создание пользователя.

```
curl -X 'POST' \
  'http://localhost:8000/auth/register/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "testuser13",
  "password": "testuserpassword"
}'

```

## 2. Авторизуйтесь в системе.

```
curl -X 'POST' \
  'http://localhost:8000/auth/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "testuser13",
  "password": "testuserpassword"
}'
```

## 3. Проверить работу авторизации:

```
curl -X 'GET' \
  'http://localhost:8000/user/my_profile' \
-H 'accept: application/json'
```

_**Если Вы успешно вошли в систему, Вы получите информацию о пользователе(себе).\
Если нет, получите ошибку.**_

## Технологический стэк:
**1. Python 3.12**\
**2. FastAPI**\
**3. Docker**\
**4. Docker Compose**\
**5. PostgreSQL**\
**6. PyTest**\
**7. Grafana**\
**8. Prometheus**


