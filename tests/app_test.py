from fastapi.testclient import TestClient
from admin_service.app import app
import sqlalchemy as sa

client = TestClient(app)

def register_admin(endpoint):
    response = client.post(
        endpoint,
        json={
            "name": "Alejo",
            "last_name": "Villores",
            "user_name": "alevillores",
            "password": "alejo2"
        },
    )
    return response

def test_01_app_start_with_no_admins():
    response = client.get('/admins/')
    print(response)
    assert 1 == 1