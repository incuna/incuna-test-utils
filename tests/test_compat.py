from unittest import TestCase

import pytest

from incuna_test_utils import compat


@pytest.fixture(scope='module')
def testcase():
    """Return a TestCase instance with python 3 assert methods."""
    class Python2AssertTestCase(compat.Python2AssertMixin, TestCase):
        """A TestCase with python 3 asserts available."""

    # Python 2 doesn't allow instantiation of a TestCase without a
    # specified test method, so specify a method known to exist on
    # all TestCase instances. We don't care which method this is.
    return Python2AssertTestCase(methodName='__init__')


def test_assert_count_equal(testcase):
    """
    Check assertCountEqual is available on a TestCase with Python2AssertMixin.
    """
    testcase.assertCountEqual((1, 1, 2), (1, 2, 1))

    with pytest.raises(AssertionError):
        testcase.assertCountEqual((1, 1, 2), (2, 1, 2))


def test_assert_regex(testcase):
    """
    Check assertRegex is available on a TestCase with Python2AssertMixin.
    """
    testcase.assertRegex('foo-bar', '[a-z]+')

    with pytest.raises(AssertionError):
        testcase.assertRegex('foo-bar', '[A-Z]+')
