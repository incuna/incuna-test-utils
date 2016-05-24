import django


DJANGO_GTE_19 = django.VERSION >= (1, 9)


class Python2AssertMixin(object):
    """
    Add python 3 asserts to python 2 TestCase

    Asserts added:
    * assertCountEqual
    * assertRegex
    """

    def __init__(self, *args, **kwargs):
        super(Python2AssertMixin, self).__init__(*args, **kwargs)
        if not hasattr(self, 'assertCountEqual'):
            self.assertCountEqual = self.assertItemsEqual

        if not hasattr(self, 'assertRegex'):
            self.assertRegex = self.assertRegexpMatches
