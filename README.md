# To run

virtualenv --python=/usr/bin/python3 .venv

source .venv/bin/activate

pip install -r requirements.txt

./docker/docker-compose up -d

env \`cat ./docker/.env\` python manage.py migrate

env \`cat ./docker/.env\` python manage.py createsuperuser

env \`cat ./docker/.env\` python manage.py runserver


запустить комманду импорта данных:

env \`cat ./docker/.env\` python manage.py -l LINK

где LINK - ссылка на log файл веб-сервера apache

например:

env \`cat ./docker/.env\` python manage.py -l http://yandex.ru/access.log

поиск работает в api (поля для поиска задаются в viewsets):

http://127.0.0.1:8000/api/v1/parsed_data/?search=blablabla
