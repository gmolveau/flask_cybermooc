#!/bin/sh

clean() {
  deactivate
  rm -rf venv .idea
	find . -type d -name __pycache__ -a -prune -exec rm -rf {} \;
}

run() {
	FLASK_ENV=development FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
}

setup() {
	clean
	virtualenv venv -p python3
	. ./venv/bin/activate
	pip install -r requirements.txt --user
}

case "$1" in
  "setup")
    setup
    ;;
  "clean")
    clean
    ;;
  "run")
    run
    ;;
  *)
	echo "unknown command"
    echo "expected: setup / clean / run"
    exit 1
    ;;
esac
exit 0
