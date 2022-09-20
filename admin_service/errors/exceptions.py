class AdminInfoException(Exception):
    ...


class AdminAlreadyExists(AdminInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Admin already exists"


class AdminBadCredentials(AdminInfoException):
    def __init__(self):
        self.status_code = 401
        self.detail = "The username/password is incorrect"


class AdminNotFoundError(AdminInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "The admin does not exists"
