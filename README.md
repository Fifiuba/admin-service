[![GitHub Workflow Status](https://github.com/Fifiuba/admin-service/actions/workflows/test_action.yml/badge.svg?event=push)](https://github.com/Fifiuba/admin-service/commits/main)
[![codecov](https://codecov.io/gh/Fifiuba/admin-service/branch/main/graph/badge.svg?token=RQXZSBLB86)](https://codecov.io/gh/Fifiuba/admin-service)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Fifiuba/admin-service/blob/develop/LICENSE)

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://backend-alejovillores.cloud.okteto.net/)

## Information
1. **Instalation**
2. **Service's purpose**
3. **Implementation Details**


### Instalation

Python's version
```shell
python --version
Python 3.8.5
 ```

[Poetry](https://python-poetry.org/)'s version
```bash
poetry --version
Poetry (version 1.2.0)
 ```

Start server locally
```bash
poetry install
poetry run uvicorn admin_service.main:app --reload
```

Test
```bash
poetry run pytest
```

Linter
```bash
poetry run black <carpeta>
```

Pasos para correr el linter
```bash
poetry run flake8 <carpeta>
```

Start server using Docker
```bash
docker-compose build --no-cache
clear
docker-compose up
```

Shut down server 
```bash
docker-compose down -v

```
#### SQL Database

* Postgres

### Service's purpose*
---

CRUD admin services, responsable for managin admins. It uses [Google Firebase](https://firebase.google.com/?hl=es) for authentication

 
_SUPER ADMIN_\
**email**: admin@fiuba.com\
**password**: adminfiuba

|Name                | Email                |
|--------------------|----------------------|
| Alejo villores     | avillores@fi.uba.ar  |

### Implementation Details
---
Class diagram

![uml](uml.png)

Secuence 

![](secuence.png)
