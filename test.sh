RUN_ENV='test' poetry run pytest -v --capture=no --cov=admin_service tests/ --cov-report=xml
