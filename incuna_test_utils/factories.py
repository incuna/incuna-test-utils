import factory

from django.contrib.auth import get_user_model


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_user_model()
    email = factory.Sequence(lambda i: 'email{}@example.com'.format(i))
    name = factory.Sequence(lambda i: 'Test User {}'.format(i))
