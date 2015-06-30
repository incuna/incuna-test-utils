from contextlib import contextmanager
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


TEST_SERVER = 'http://testserver'


def next_mro_class(cls, current):
    """Find the next class in `cls.mro()` after `current`."""
    mro = cls.mro()
    return mro[mro.index(current) + 1]


def import_path(cls):
    """Return the import path for a class."""
    return '{}.{}'.format(cls.__module__, cls.__name__)


@contextmanager
def isolate_method(cls, mixin, method_name, parent_return_value=None):
    """Isolate a method's implementation from its inheritance hierarchy."""
    parent_class_path = import_path(next_mro_class(cls, mixin))
    parent_method_path = '{}.{}'.format(parent_class_path, method_name)

    with patch(parent_method_path) as method:
        method.return_value = parent_return_value
        yield getattr(mixin, method_name)


def field_names(model):
    """Return a set of all field names for a model."""
    try:
        fields = model._meta.get_fields()
    except AttributeError:
        return set(model._meta.get_all_field_names())
    return {field.name for field in fields}
