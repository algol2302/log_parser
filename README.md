# TODO

virtualenv --python=/usr/bin/python3 .venv

source .venv/bin/activate

pip install -r requirements.txt

./docker/docker-compose up -d

env \`cat ./docker/.env\` python manage.py migrate

env \`cat ./docker/.env\` python manage.py createsuperuser

env \`cat ./docker/.env\` python manage.py runserver
