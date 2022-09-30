from fastapi import status
from fastapi.testclient import TestClient
from admin_service.app import app
from admin_service.security import jwt_handler
from admin_service.database import schemas, database, crud


class TestAcceptance:
    token = jwt_handler.create_access_token(1, True)
    client = TestClient(app)

    def register_admin(self, endpoint):
        response = self.client.post(
            endpoint,
            json={
                "name": "Alejo",
                "last_name": "Villores",
                "email": "alevillores@hotmail.com",
                "password": "alejo2",
            },
            headers={"Authorization": f"Bearer {self.token}"},
        )
        return response

    def create_people(self, n):
        admins = []
        for i in range(n):
            admins.append(
                schemas.AdminRequest(
                    name="admin",
                    last_name="admin",
                    email=f"{i}@gmail.com",
                    password="test",
                )
            )
        db = database.get_local_session()
        for admin in admins:
            crud.create_admin(admin, "token_id", db)

    def test_01_app_start_with_no_admins(self):
        response = self.client.get(
            "admins/", headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data == []

    def test_03_when_loggin_in_admin_it_should_return_token(self):
        self.register_admin("admins/")
        login_response = self.client.post(
            "admins/login",
            json={
                "token": "kEqofVcDh1bw4lzQkdFSXr4VvLu1",
            },
        )
        assert login_response.status_code == status.HTTP_200_OK, login_response.text
        data = login_response.json()
        actual = jwt_handler.decode_token(data["token"])
        expected = {
            "id": 1,
            "admin": True,
        }

        assert actual["id"] == expected["id"]
        assert actual["admin"] == expected["admin"]

    def test_04_should_be_able_to_see_profile_of_one_admin(self):
        response = self.client.get(
            "admins/1", headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == status.HTTP_200_OK

        data = response.json()

        assert data["id"] == 1
        assert data["name"] == "Alejo"
        assert data["last_name"] == "Villores"
        assert data["email"] == "alevillores@hotmail.com"

    def test_05_admin_not_found_should_raise_http_error_code_404(self):
        response = self.client.get(
            "admins/100", headers={"Authorization": f"Bearer {self.token}"}
        )
        data = response.json()
        assert response.status_code == status.HTTP_404_NOT_FOUND, response.text
        assert data["detail"] == "The admin does not exists"

    def test_06_admin_already_exists_should_raise_http_error_code_409(self):
        response = self.register_admin("admins/")
        data = response.json()
        assert response.status_code == status.HTTP_409_CONFLICT, response.text
        assert data["detail"] == "Admin already exists"

    def test_07_when_loggin_with_bad_credentials_should_get_401_error(self):

        response = self.client.post(
            "admins/login",
            json={"token": "token"},
        )
        assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE, response.text
        data = response.json()
        assert data["detail"] == "The username/password is incorrect"

    def test_08_get_admins_should_have_authorazation(self):
        response = self.client.get(
            "admins/", headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == status.HTTP_200_OK

    def test_09_as_logged_user_i_can_se_my_profile(self):
        login_response = self.client.post(
            "admins/login",
            json={"token": "toke"},
        )
        assert login_response.status_code == status.HTTP_200_OK, login_response.text

        token = login_response.json()["token"]
        response = self.client.get(
            "admins/me/", headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == status.HTTP_200_OK, response.text
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "Alejo"
        assert data["last_name"] == "Villores"
        assert data["email"] == "alevillores@hotmail.com"

    def test_10_user_with_no_token_cant_register(self):
        response = self.client.post(
            "admins/",
            json={
                "name": "Test",
                "last_name": "test",
                "email": "testin@hotmail.com",
                "password": "tes",
            },
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.text
        data = response.json()
        assert data["detail"] == "Unauthorized"

    def test_11_should_five_admins_registered(self):
        self.create_people(4)
        response = self.client.get(
            "admins/", headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 5

    def test_12_user_named_alejo_change_last_name(self):
        me = self.client.get(
            "admins/1", headers={"Authorization": f"Bearer {self.token}"}
        )
        assert me.status_code == status.HTTP_200_OK, me.text
        data = me.json()
        assert data["last_name"] == "Villores"

        response = self.client.patch(
            "admins/me/",
            json={"name": data.get("name"), "last_name": "Villares"},
            headers={"Authorization": f"Bearer {self.token}"},
        )
        assert response.status_code == status.HTTP_202_ACCEPTED, response.text
        patched = response.json()
        assert patched["last_name"] == "Villares"

    def test_13_delete_admin_from_db(self):
        id_eliminated = self.client.delete(
            "/admins/1", headers={"Authorization": f"Bearer {self.token}"}
        )
        assert id_eliminated.status_code == status.HTTP_202_ACCEPTED
        deleted = id_eliminated.json()
        assert deleted["id"] == 1
