class RecordMock:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def uid():
        return 1


class FirebaseMock:
    def create_admin(email, password, app):
        return RecordMock(email, password)
