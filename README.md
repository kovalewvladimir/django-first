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

settings.py
```
# LDAP
AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',]


# Ldap auth
AUTH_LDAP_SERVER_URI = "ldap://192.168.0.30"
AUTH_LDAP_BIND_DN = "cn=django_user,cn=Users,dc=vld,dc=local"
AUTH_LDAP_BIND_PASSWORD = "Qwert123"
AUTH_LDAP_USER_SEARCH = LDAPSearch("cn=Users,dc=vld,dc=local",
    ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}


# Search group
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("cn=Users,dc=vld,dc=local",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
AUTH_LDAP_REQUIRE_GROUP = "cn=django_group,cn=Users,dc=vld,dc=local"


# Logger
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
```

Исправление ошибки: `fatal error: lber.h`
```sh
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```

## Apache

Установка Apache2
```sh
sudo aptitude install libapache2-mod-wsgi
```

Установка модуля Apache mod-wsgi 
TODO: aptitude что это?
```sh
sudo aptitude install libapache2-mod-wsgi
```

Создаём virtual host:
```sh
sudo nano /etc/apache2/sites-available/domain1.com.conf


<VirtualHost *:80>
        ServerName domain1.com
        ServerAlias www.domain1.com
        WSGIScriptAlias / /home/vek/djangoenv/firstapp/firstapp.wsgi
</VirtualHost>
```
