#!/bin/bash

# sudo docker exec -i web bash -c "chmod -R 755 /usr/src/static && chmod -R 755 /root"
# sudo docker exec -i web bash -c "cd /usr/src/app/react && npm install && npm run collect"
echo "## Start static files collection"
docker compose exec web python manage.py collectstatic --no-input
echo "## Start migration process"
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
# sudo docker-compose exec nginx chmod -R 755 /static
echo "## Create superuser"
docker compose exec web python manage.py createsuperuser