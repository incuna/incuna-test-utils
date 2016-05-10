from mock import patch

from .utils import is_django_gte_19


@patch('tests.testcases.utils.django')
def test_is_django_gte_19(django):
    django.VERSION = (1, 9)
    assert is_django_gte_19() is True


@patch('tests.testcases.utils.django')
def test_is_django_lt_19(django):
    django.VERSION = (0, 96)
    assert is_django_gte_19() is False
