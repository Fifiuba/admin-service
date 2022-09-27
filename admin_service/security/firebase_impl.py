from firebase_admin import exceptions as fb_exceptions
from admin_service.errors import exceptions


class Firebase:
    def __init__(self, auth, app):
        self.auth = auth
        self.app = app

    def create_admin(self, admin):
        try:
            user_record = self.auth.create_user(
                email=admin.email,
                password=admin.password,
                display_name=admin.last_name,
                app=self.app,
            )
        except (ValueError, fb_exceptions.FirebaseError):
            raise exceptions.AdminBadCredentials
        else:
            return user_record.uid

    def delete_admin(self, uid: str):
        try:
            self.auth.delete_user(uid, app=self.app)
        except (ValueError, fb_exceptions.FirebaseError):
            raise exceptions.AdminNotDeleted

    def valid_admin(self, admin):
        try:
            dic = self.auth.verify_id_token(admin.token, app=self.app)

        except (
            self.auth.UserDisabledError,
            self.auth.CertificateFetchError,
            self.auth.RevokedIdTokenError,
        ):

            raise exceptions.AdminBadCredentials
        except (
            self.auth.ExpiredIdTokenError,
            self.auth.InvalidIdTokenError,
            ValueError,
        ):

            raise exceptions.AdminBadCredentials
        else:
            return dic.get("email"), dic.get("uid")
