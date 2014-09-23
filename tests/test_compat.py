from mock import patch
import sys
from unittest import TestCase

import pytest

from incuna_test_utils import compat


def test_wipe_id_fields_lt_17():
    fields = ['foo', 'foo_id']
    expected_fields = ['foo']

    with patch.object(compat, 'DJANGO_LT_17', new=True):
        wiped_fields = compat.wipe_id_fields_on_django_lt_17(fields)
        assert wiped_fields == expected_fields


def test_wipe_id_fields_gte_17():
    fields = ['foo', 'foo_id']

    with patch.object(compat, 'DJANGO_LT_17', new=False):
        wiped_fields = compat.wipe_id_fields_on_django_lt_17(fields)
        assert wiped_fields == fields


@pytest.fixture(scope='module')
def testcase():
    class Python2AssertTestCase(compat.Python2AssertMixin, TestCase):
        pass

    return Python2AssertTestCase()


@pytest.mark.skipif(sys.version_info >= (3,), reason='Requires python 2')
def test_python2_count_equal(testcase):
    assert testcase.assertCountEqual == testcase.assertItemsEqual


@pytest.mark.skipif(sys.version_info < (3,), reason='Requires python 3')
def test_python3_count_equal(testcase):
    assert hasattr(testcase, 'assertCountEqual')


@pytest.mark.skipif(sys.version_info >= (3,), reason='Requires python 2')
def test_python2_regex(testcase):
    assert testcase.assertRegex == testcase.assertRegexpMatches


@pytest.mark.skipif(sys.version_info < (3,), reason='Requires python 3')
def test_python3_regex(testcase):
    assert hasattr(testcase, 'assertRegex')
