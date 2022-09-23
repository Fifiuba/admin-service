import re
from admin_service.errors import exceptions

validator = re.compile(r"^(Bearer\s)(.*)")


def is_auth(headers):
    header = headers.get("authorization")
    if header is None or not validator.match(header):
        raise exceptions.AdminUnauthorized
    else:
        header = headers.get("authorization")
        _b, token = validator.search(header).groups()
        return token
