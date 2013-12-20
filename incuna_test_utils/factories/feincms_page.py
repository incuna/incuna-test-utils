import factory

from feincms.module.page.models import Page


class PageFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Page
    title = factory.Sequence(lambda n: 'Page {0}'.format(n))
    slug = factory.Sequence(lambda n: 'page-{0}'.format(n))
