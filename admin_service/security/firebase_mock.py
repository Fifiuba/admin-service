class FirebaseMock:
    token = "asdasdasdslwlewed1213123"

    def create_admin(self, admin, app="def"):
        return self.token

    def valid_admin(self, admin):
        if admin.token == "token":
            return "bad@credentials", self.token

        return "alevillores@hotmail.com", self.token

    def delete_admin(self, uid):
        pass
