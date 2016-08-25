# Первый проект на django
## Инструкция 

Установка easy_install (Система управления пакетами Python)
```sh
sudo apt-get install python-setuptools
```

Установка виртуального окружения virtualenv
```sh
sudo easy_install virtualenv
```

Настройка виртуального окружения

Ключ `--no-site-packages` не использовать системные библиотеки python

Ключ `-p python3` для python3 
djangoent - имя папки виртуального окружения
```sh
virtualenv --no-site-packages djangoenv
```

Переходим в папку djangoent
```sh
cd djangoenv
```

Активируем виртуальное окружение Python
```sh
source bin/activate
```

Установка django в виртуальное окружение
```sh
easy_install django
```

Создание проекта firstapp
```sh
python bin/django-admin.py startproject firstapp
```

Переходим в папку firstapp
```sh
cd firstapp
```

Создать суперпользователя
```sh
python manage.py createsuperuser
```

Запускаем сервер
```sh
python manage.py runserver
```

Создание проекта article
```sh
python manage.py startapp article
```

Зафиксировать миграцию 
```sh
python manage.py makemigrations
```

Миграция базы данных
```sh
python manage.py migrate
```

Откат миграции бд 

`article` - имя арр

`0002` - версия миграции
```sh
python manage.py migrate article 0002
```

## LDAP

Исправление ошибки: `fatal error: lber.h`
```sh
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```
