import pytest
from admin_service.security import authorization, jwt_handler
from admin_service.errors import exceptions


class TestSecurity:
    def test_01_correct_header_does_not_throw_exception(self):
        fake_token = jwt_handler.create_access_token(1, "admin")
        header = {"authorization": f"Bearer {fake_token}"}
        token_id = authorization.is_auth(header)
        assert token_id == 1

    def test_02_incorrect_header_auth_raise_exception(self):
        header = {"authorization": "NotCorrect very_long_token"}
        with pytest.raises(exceptions.AdminUnauthorized):
            authorization.is_auth(header)

    def test_03_incorrect_auth_raise_exception(self):
        header = {"x-header": "Bearer very_long_token"}
        with pytest.raises(exceptions.AdminUnauthorized):
            authorization.is_auth(header)
