from fastapi.testclient import TestClient
from fastapi import status
from admin_service.app import app
from admin_service.security import jwt_handler, password_hasher
from admin_service.database import schemas, database, crud


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


def test_02_when_creating_new_admin_it_should_have_encripted_pass():
    response = register_admin("admins/")

    assert response.status_code == status.HTTP_201_CREATED, response.text
    data = response.json()
    assert password_hasher.verify_password("alejo2", data["password"]) is True


def test_03_when_loggin_in_admin_it_should_return_token():

    login_response = client.post(
        "admins/login", json={"user_name": "alevillores", "password": "alejo2"}
    )
    assert login_response.status_code == status.HTTP_200_OK, login_response.text
    data = login_response.json()
    actual = jwt_handler.decode_token(data["token"])
    expected = {
        "id": 1,
        "admin": True,
    }

    assert actual == expected


def test_04_should_be_able_to_see_profile_of_one_admin():
    admins = []
    for i in range(3):
        admins.append(
            schemas.AdminRequest(
                name="admin", last_name="admin", user_name=str(i), password="test"
            )
        )
    db = database.get_local_session()
    for admin in admins:
        crud.create_admin(admin, db)

    response = client.get("admins/1")
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    expected = {
        "id": 1,
        "name": "Alejo",
        "last_name": "Villores",
        "user_name": "alevillores",
    }
    assert data["id"] == expected["id"]
    assert data["name"] == expected["name"]
    assert data["last_name"] == expected["last_name"]
    assert data["user_name"] == expected["user_name"]
    assert password_hasher.verify_password("alejo2", data["password"]) is True


def test_05_admin_not_found_should_raise_http_error_code_404():
    response = client.get("admins/100")
    data = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text
    assert data["detail"] == "The admin does not exists"


def test_06_admin_already_exists_should_raise_http_error_code_409():
    response = register_admin("admins/")
    data = response.json()
    assert response.status_code == status.HTTP_409_CONFLICT, response.text
    assert data["detail"] == "Admin already exists"


def test_03_when_loggin_with_bad_credentials_should_get_401_error():

    response = client.post(
        "admins/login", json={"user_name": "alevillores", "password": "mal_password"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.text
    data = response.json()
    assert data["detail"] == "The username/password is incorrect"


# def test():
#    token = jwt_handler.create_access_token(1, True)
#    response = client.get("admins/",headers={'Authorization': f'Baerer {token}'})
#    assert response.status_code == status.HTTP_200_OK
#    data = response.json()
#    assert 1 == 1
