from django.contrib.auth.models import User
import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence('User {}'.format)

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        self.raw_password = extracted or 'default_password'
        self.set_password(self.raw_password)
        if create:
            self.save()
