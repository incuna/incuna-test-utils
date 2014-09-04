import factory

from feincms.module.page.models import Page


class PageFactory(factory.DjangoModelFactory):
    title = factory.Sequence('Page {0}'.format)
    slug = factory.Sequence('page-{0}'.format)

    class Meta:
        model = Page
