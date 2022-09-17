from fastapi.testclient import TestClient
from fastapi import status
from admin_service.app import app
from admin_service.database.database import get_db, engine
from admin_service.database.models import Base
from admin_service.security import password_hasher,jwt_handler
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa


client = TestClient(app)


def register_admin(endpoint):
    response = client.post(
        endpoint,
        json={
            "name": "Alejo",
            "last_name": "Villores",
            "user_name": "alevillores",
            "password": "alejo2",
        },
    )
    return response


def test_01_app_start_with_no_admins():
    response = client.get("admins/")
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data == []


def test_02_when_creating_new_admin_it_should_return_token():
    response = register_admin("admins/new")

    assert response.status_code == status.HTTP_201_CREATED, response.text
    data = response.json()
    expected = {
        "id": 1,
        "admin": True,
    }
    actual = jwt_handler.decode_token(data['token'])
    
    assert actual == expected




