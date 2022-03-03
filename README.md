# django_link_shortner

Простой сайт на [Django](https://www.djangoproject.com/) и [Django REST Framework](https://www.django-rest-framework.org/) для создания сокращенных ссылок.

Пример сайта доступен по адресу [short.efremov.xyz](http://short.efremov.xyz).

## Установка
Вам понадобится установленный Python 3.8+ и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/django_link_shortner
```

Создайте в этой папке виртуальное окружение:
```bash
$ cd django_link_shortner
$ python3 -m venv venv
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Использование

### Переменные среды
Заполните файл .env.example и переименуйте его в .env или иным образом задайте переменные среды:
* `DEBUG` - включен ли режим дебага в Django. По умолчанию - `True`.
* `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts). По умолчанию - `127.0.0.1`.
* `SECRET_KEY` - секретный ключ отвечающий за шифрование. По умолчанию - `REPLACE_ME`. 
* `GENERATE_SHORT_URL_BYTES` - число байт используемых для генерации случайной короткой ссылки. По умолчанию - 3.
* `GENERATE_SHORT_URL_MAX_RETRIES` - число неудачных попыток, после которого будет увеличено на единицу значение `GENERATE_SHORT_URL_BYTES`. По умолчанию - 5.

### Миграции базы данных
Перед тем как запускать сайт нужно применить миграции базы данных. Находясь в директории django_link_shortner исполните:
```bash
$ venv/bin/python manage.py migrate
```

### Запуск сайта
Находясь в директории django_link_shortner исполните:
```bash
$ venv/bin/python manage.py runserver
```

Сайт запустится по адресу [127.0.0.1:8000](http://127.0.0.1:8000).

Можно указать желаемый IP-адрес и порт:
```bash
$ venv/bin/python manage.py runserver 127.0.0.1:8000
```
