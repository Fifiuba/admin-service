import os

if "RUN_ENV" in os.environ.keys() and os.environ["RUN_ENV"] == "test":
    # read from .env file, if DATABASE_URL does not exist
    # then read from system env
    from admin_service.security.firebase_mock import FirebaseMock

    firebase = FirebaseMock()
    default_app = "def"
else:
    from admin_service.security.firebase_impl import Firebase
    import firebase_admin
    from firebase_admin import credentials, auth

    cred = credentials.Certificate("admin_service/security/firebase_keys.json")
    default_app = firebase_admin.initialize_app(cred, name="test")

    # Initialize the default app
    default_app = firebase_admin.initialize_app(cred)
    firebase = Firebase(auth, default_app)


def get_fb():
    try:
        yield firebase
    finally:
        firebase
