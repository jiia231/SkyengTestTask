#!/bin/bash

while true; do
  python3 src/manage.py check --database default > /dev/null 2> /dev/null
  exit_code=$?
  sleep 2
  if [ $exit_code -eq 0 ]; then
    break
  fi
done

python3 src/manage.py migrate --no-input

python3 src/manage.py collectstatic --no-input

gunicorn --chdir ./src config.wsgi:application --bind 0.0.0.0:8000
