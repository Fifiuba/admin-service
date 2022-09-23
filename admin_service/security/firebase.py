import os


if "RUN_ENV" in os.environ.keys() and os.environ["RUN_ENV"] == "test":
    # read from .env file, if DATABASE_URL does not exist
    # then read from system env
    from admin_service.security.firebase_mock import FirebaseMock

    firebase = FirebaseMock()
    default_app = "def"
else:

    from admin_service.errors import exceptions
    import firebase_admin
    from firebase_admin import credentials, auth
    from firebase_admin import exceptions as fb_exceptions

    cred = credentials.Certificate("admin_service/security/firebase_keys.json")
    default_app = firebase_admin.initialize_app(cred, name="test")

    # Initialize the default app
    default_app = firebase_admin.initialize_app(cred)


def create_admin(email: str, password: str):
    try:
        user_record = auth.create_user(email=email, password=password, app=default_app)
    except (ValueError, fb_exceptions.FirebaseError):
        raise exceptions.AdminBadCredentials
    else:
        return user_record.uid


# def valid_admin(admin):
#     try:
#         user_record = auth.get_user(admin.password, default_app)
#     except (ValueError, auth.UserNotFoundError, fb_exceptions.FirebaseError):
#         raise exceptions.AdminBadCredentials
#     else:
#         return user_record.email, user_record.uid


def get_fb():
    try:
        yield firebase
    finally:
        firebase
