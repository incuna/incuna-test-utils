import factory

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:  # Django 1.4
    from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    email = factory.Sequence(lambda i: 'email{}@example.com'.format(i))
    name = factory.Sequence(lambda i: 'Test User {}'.format(i))
