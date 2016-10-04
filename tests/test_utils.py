from incuna_test_utils import utils

from .models import User


class Parent(object):
    def method(self):
        return {'foo'}


class Mixin(object):
    def method(self):
        data = super(Mixin, self).method()
        data.add('bar')
        return data


class Child(Mixin, Parent):
    pass


def test_next_mro_class():
    assert utils.next_mro_class(Child, Mixin) == Parent


def test_import_path():
    assert utils.import_path(Child) == 'tests.test_utils.Child'


def test_isolate_method():
    """isolate_method allows testing a method independent of its parents."""
    instance = Child()
    assert instance.method() == {'foo', 'bar'}

    isolate_mixin_method = utils.isolate_method(
        Child,
        mixin=Mixin,
        method_name='method',
        parent_return_value=set(),
    )
    with isolate_mixin_method as method:
        assert method(instance) == {'bar'}


def test_field_names():
    fields = utils.field_names(User)
    assert fields == {'id', 'email', 'name'}


def test_get_all_field_names():
    fields = utils.get_all_field_names(User)
    assert isinstance(fields, list)
    # Convert to set as list could complain about ordering in equality check
    assert set(fields) == {'id', 'email', 'name'}
