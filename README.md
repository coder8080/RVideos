## RVideos
Простой видеохостинг, написанный на python django

## Системные требования
- Актуальный и рабочий терминал (Пк, android + termux и др.)
- python >= 3.7
- pip последней версии

## Как запустить сайт RVideos
Выполните следующие команды
```bash
git clone https://github.com/coder8080/RVideos
cd ./RVideos
pip install -r requirements.txt
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py createsuperuser
```
Если вышеперечисленные команды не работают, проверьте, соблюдены ли системные требования. Если да, то попробуйте вместо python и pip python3 и pip3.

Так же необходимо сгенерировать секретный ключ (ключ безопасности) сайта. Сделать это можно с помощью сайта
https://djecrety.ir/.
Затем полученный ключ необходимо вставить в кавычки на 23 строке файла disk/setting.py вместо слов "insert secret key here"

После всех вышеперечисленных действий вы можете запустить сайт:
```bash
python ./manage.py runserver
```

## Настройка сайта
По умолчанию сайт настроен на работу на сайте localhost. Если вы хотите использовать его на сервере с другим ip, то допишите адрес, на котором будет работать сайт в массив ALLOWED_HOSTS в 25 строке файла disk/setting.py, а так же в конец команды запуска сервера. Пример:
```
python ./manage.py runserver 192.168.0.5
```

## Виртуальное окружение
Если вы хотите, чтобы проект использовал виртуальное окружение, то вам необходимо выполнить следующие команды:
```bash
pip install virtualenv
python -m virtualenv venv
source ./venv/bin/activate
pip install -r ./requirements.txt
python manage.py runserver
```

P. S.
Проект ещё развивается, поэтому если у вас есть какие-либо мысли по направлению дальнейшего развития, идеи или баги прошу в раздел issues.
Удачного использования!