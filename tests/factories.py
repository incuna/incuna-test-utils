from django.contrib.auth.models import User
import factory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence('User {}'.format)

    class Meta:
        model = User

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        self.raw_password = 'default_password' if extracted is None else extracted
        self.set_password(self.raw_password)
        if create:
            self.save()
