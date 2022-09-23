import pytest
from admin_service.security import authorization
from admin_service.errors import exceptions


class TestSecurity:
    def test_01_correct_header_does_not_throw_exception(self):
        header = {"authorization": "Bearer very_long_token"}
        token = authorization.is_auth(header)
        assert token == "very_long_token"

    def test_02_incorrect_header_auth_raise_exception(self):
        header = {"authorization": "NotCorrect very_long_token"}
        with pytest.raises(exceptions.AdminUnauthorized):
            authorization.is_auth(header)

    def test_03_incorrect_auth_raise_exception(self):
        header = {"x-header": "Bearer very_long_token"}
        with pytest.raises(exceptions.AdminUnauthorized):
            authorization.is_auth(header)
