from contextlib import contextmanager
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from django.apps import apps
from django.core.checks import Error
from django.core.checks.registry import registry


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


class AssertCheckErrorMixin:
    """Add assert method to validate `check` error."""
    def assert_check_error(self, message, error_id, check_method, hint=None, obj=None):
        """Assert `check_method` error raises as expected."""
        app_config = apps.get_app_config(self.app_config_name)
        expected_error = Error(
            msg=message,
            hint=hint,
            obj=obj if obj is not None else app_config,
            id=error_id,
        )

        errors = check_method([app_config])
        self.assertIn(expected_error, errors)

    def assert_check_passes(self, check_method, msg=None):
        """Assert check does not return an error."""
        config = apps.get_app_config(self.app_config_name)
        errors = check_method([config])
        self.assertEqual(errors, [], msg=msg)

    def assert_check_other_config(self, check_method, msg=None):
        """Assert `check_method` returns `[]` for other config."""
        self.assertEqual(check_method([]), [], msg=msg)

    def assert_check_registered(self, check_method, msg=None):
        """Assert `check_method` is registered."""
        self.assertIn(check_method, registry.registered_checks, msg=msg)
