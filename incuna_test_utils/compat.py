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
        return filter(lambda n: not n.endswith('_id'), fields)
    return fields


class Python2CountEqualMixin(object):
    """Add assertCountEqual to python 2 TestCase"""
    def __init__(self, *args, **kwargs):
        super(Python2CountEqualMixin, self).__init__(*args, **kwargs)
        if not hasattr(self, 'assertCountEqual'):
            self.assertCountEqual = self.assertItemsEqual
