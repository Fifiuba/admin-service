from firebase_admin import exceptions as fb_exceptions
from admin_service.errors import exceptions

class Firebase:
    def __init__(self,auth,app):
        self.auth = auth
        self.app = app
    
    def create_admin(self,email: str, password: str):
        try:
            user_record = self.auth.create_user(email=email, password=password, app=self.app)
        except (ValueError, fb_exceptions.FirebaseError):
            raise exceptions.AdminBadCredentials
        else:
            return user_record.uid

    def delete_admin(self,uid: str):
        try:
            self.auth.delete_user(uid, app=self.app)
        except (ValueError, fb_exceptions.FirebaseError):
            raise exceptions.AdminNotDeleted