from django.contrib.auth.models import User
import factory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence('User {}'.format)

    class Meta:
        model = User
