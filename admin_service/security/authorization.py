import re
from admin_service.errors import exceptions

validator = re.compile(r"^(Baerer\s)(.*)")
# Matchea que inicie con Barear
# que luego tenga un espacion(\s)
# 1 o mas caracteres (token)


def is_auth(headers):
    header = headers.get("authorization")
    if header is None or not validator.match(header):
        raise exceptions.AdminUnauthorized


def get_token(headers):
    header = headers.get("authorization")
    _b, token = validator.search(header).groups()
    return token
