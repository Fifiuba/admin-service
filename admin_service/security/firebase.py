# Import the Firebase service
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import exceptions as fb_exceptions

from admin_service.errors import exceptions

cred = credentials.Certificate("admin_service/security/firebase_keys.json")
default_app = firebase_admin.initialize_app(cred, name="test")

# Initialize the default app
default_app = firebase_admin.initialize_app(cred)
print(default_app.name)


def create_admin(email: str, password: str):
    try:
        user_record = auth.create_user(email=email, password=password, app=default_app)
    except (ValueError, fb_exceptions.FirebaseError):
        raise exceptions.AdminBadCredentials
    else:
        return user_record.uid


def valid_admin(admin):
    try:
        user_record = auth.get_user(admin.password, default_app)
    except (ValueError, auth.UserNotFoundError, fb_exceptions.FirebaseError):
        raise exceptions.AdminBadCredentials
    else:
        return user_record.email, user_record.uid
