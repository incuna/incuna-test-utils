import factory


class BaseUserFactory(factory.DjangoModelFactory):
    email = factory.Sequence('email{}@example.com'.format)
