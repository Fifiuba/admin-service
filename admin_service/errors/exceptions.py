class AdminInfoException(Exception):
    ...


class AdminAlreadyExists(AdminInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Admin already exists"


class AdminBadCredentials(AdminInfoException):
    def __init__(self):
        self.status_code = 406
        self.detail = "The username/password is incorrect"


class AdminUnauthorized(AdminInfoException):
    def __init__(self):
        self.status_code = 401
        self.detail = "Unauthorized"


class AdminNotFoundError(AdminInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "The admin does not exists"


class AdminNotDeleted(AdminInfoException):
    def __init__(self):
        self.status_code = 500
        self.detail = "Admin not deleted because internal problems"
