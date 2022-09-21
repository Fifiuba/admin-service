poetry run black .
poetry run flake8 .
RUN_ENV='test' poetry run pytest -v --capture=no