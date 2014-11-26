import pytest

from incuna_test_utils.factories.user import BaseUserFactory
from tests.models import User


class UserFactory(BaseUserFactory):
    class Meta:
        model = User


@pytest.mark.django_db
def test_userfactory():
    user = UserFactory.build()
    assert isinstance(user, User)
    assert 'example.com' in user.email
