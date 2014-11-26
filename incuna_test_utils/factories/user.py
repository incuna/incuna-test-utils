import factory


class BaseUserFactory(factory.DjangoModelFactory):
    email = factory.Sequence('email{}@example.com'.format)


class BaseAdminUserFactory(BaseUserFactory):
    is_active = True
    is_staff = True
    is_superuser = True

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        # By using this method password can never be set to `None`!
        self.raw_password = 'default_password' if extracted is None else extracted
        self.set_password(self.raw_password)
        if create:
            self.save()
