import re
from admin_service.errors import exceptions
from admin_service.security import jwt_handler

validator = re.compile(r"^(Bearer\s)(.*)")


def is_auth(headers):
    header = headers.get("authorization")
    if header is None or not validator.match(header):
        raise exceptions.AdminUnauthorized
    else:
        header = headers.get("authorization")
        _b, token = validator.search(header).groups()
        payload = jwt_handler.decode_token(token)
        if payload["rol"] != "admin":
            raise exceptions.AdminUnauthorized

        admin_id = payload["id"]
        return admin_id
