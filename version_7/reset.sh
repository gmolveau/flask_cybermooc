#!/bin/sh

function clean_up() {
    rm -rf venv db.sqlite
	find . -type d -name __pycache__ -a -prune -exec rm -rf {} \;
}

clean_up
virtualenv venv -p python3
. ./venv/bin/activate
pip install -r requirements.txt
FLASK_APP=. flask reset-db
FLASK_ENV=development FLASK_APP=. flask run --host=0.0.0.0 --port=5000
clean_up