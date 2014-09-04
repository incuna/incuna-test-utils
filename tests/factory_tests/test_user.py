import pytest

from ..models import User
from incuna_test_utils.factories.user import BaseUserFactory


class UserFactory(BaseUserFactory):
    class Meta:
        model = User


@pytest.mark.django_db
def test_userfactory():
    user = UserFactory.build()
    assert isinstance(user, User)
    assert 'example.com' in user.email
    assert 'Test User' in user.name
