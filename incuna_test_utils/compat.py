import django


DJANGO_LT_15 = django.VERSION < (1, 5)
DJANGO_LT_16 = django.VERSION < (1, 6)
DJANGO_LT_17 = django.VERSION < (1, 7)


def wipe_id_fields_on_django_lt_17(fields):
    """
    Remove fields ending in '_id' on Django < 1.7

    This required for tests checking the list of fields on a model because in
    Django 1.7, all the FKs appear as `other_model` and `other_model_id`.
    """
    if DJANGO_LT_17:
        return [field for field in fields if not field.endswith('_id')]
    return fields


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
