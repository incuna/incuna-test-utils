from mock import patch

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


def test_python_2_count_equal():
    class Python2TestCase(compat.Python2CountEqualMixin):
        def assertItemsEqual(self, first, second):
            pass

    testcase = Python2TestCase()
    assert hasattr(testcase, 'assertCountEqual')


def test_python3_count_equal():
    class Python3TestCase(compat.Python2CountEqualMixin):
        def assertCountEqual(self, first, second):
            pass

    testcase = Python3TestCase()
    assert hasattr(testcase, 'assertCountEqual')
