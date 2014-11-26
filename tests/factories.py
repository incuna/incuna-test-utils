import factory
from django.contrib.auth.models import User

from incuna_test_utils.factories.user import BaseAdminUserFactory, BaseUserFactory


class UserFactory(BaseUserFactory):
    username = factory.Sequence('User {}'.format)

    class Meta:
        model = User


class AdminFactory(BaseAdminUserFactory):
    username = factory.Sequence('User {}'.format)

    class Meta:
        model = User
