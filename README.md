[![GitHub Workflow Status](https://github.com/Fifiuba/admin-service/actions/workflows/test_action.yml/badge.svg?event=push)](https://github.com/Fifiuba/admin-service/commits/main)
[![codecov](https://codecov.io/gh/Fifiuba/admin-service/branch/main/graph/badge.svg?token=WQLIP37828)](https://codecov.io/gh/Fifiuba/admin-service)
[![GitHub issues](https://img.shields.io/github/issues/Fifiuba/admin-service?&style=flat-square)](https://github.com/Fifiuba/admin-service/issues)
[![GitHub license](https://img.shields.io/github/license/Fifiuba/admin-service?&style=flat-square)](https://github.com/Fifiuba/admin-service/blob/main/LICENSE)

### Instalación

Version de python
```shell
python --version
Python 3.8.5
 ```
Version de poetry
```bash
poetry --version
Poetry (version 1.2.0)
 ```

Pasos para levantar el servidor local una vez clonado el repo
```bash
poetry install
poetry run uvicorn users_service.app:app --reload
```

Pasos para correr los test
```bash
poetry run pytest
```

Pasos para correr el formatter
```bash
poetry run black <carpeta>
```

Pasos para correr el linter
```bash
poetry run flake8 <carpeta>
```