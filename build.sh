#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry export requirements.txt
poetry export -f requirements.txt --output requirements.txt --without-hashes

# install requirements
pip install -r requirements.txt

# run migrations
python manage.py migrate