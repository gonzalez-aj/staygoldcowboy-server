#!/bin/bash

rm db.sqlite3
rm -rf ./staygoldcowboyapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations staygoldcowboyapi
python3 manage.py migrate staygoldcowboyapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata art
python3 manage.py loaddata tags
python3 manage.py loaddata tickets
