class FirebaseMock:
    token = "asdasdasdslwlewed1213123"

    def create_admin(self, email, password, app="def"):
        return self.token

    def valid_admin(self, admin):
        email = admin.email
        return email, self.token
