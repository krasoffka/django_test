#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status
export PYTHONUNBUFFERED=0

case "$1" in
    createsuperuser)
        export ADMIN_ENABLED=True
        exec /usr/local/bin/gunicorn margosys.wsgi -b 0.0.0.0:8000 -w 2
    ;;

    web)
        echo ">> RUN MARGOSYS"
        python3.7 manage.py migrate
        echo ">> migrate COMPLETED"
        echo ">> filling DB"
        echo ">> filling DB COMPLETED"
        echo ">> STARTING SERVER..."
        exec python3.7 manage.py runserver 0.0.0.0:8000
    ;;

    *)
        if [ $# -eq 0 ]
          then
            echo "No arguments supplied"
            show_help
          else
            echo "Running '$1' command..."
            exec "$1"
        fi
    ;;
esac
