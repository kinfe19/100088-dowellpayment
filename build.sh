#!/usr/bin/env bash

set -o errexit  # exit on error

pip18 install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate