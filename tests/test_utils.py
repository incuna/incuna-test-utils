from incuna_test_utils import utils


class Parent:
    def method(self):
        return {'foo'}


class Mixin:
    def method(self):
        data = super().method()
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

    kwargs = {
        'mixin': Mixin,
        'method_name': 'method',
        'parent_return_value': set(),
    }
    with utils.isolate_method(Child, **kwargs) as method:
        assert method(instance) == {'bar'}
