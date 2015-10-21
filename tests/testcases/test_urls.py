import pytest

from incuna_test_utils.testcases.urls import URLTestCase

from .. import other_views, views


class TestURLTestCase(URLTestCase):
    def test_assert_url_matches_view(self):
        self.assert_url_matches_view(
            view=views.my_view,
            expected_url='/',
            url_name='function-view',
        )

    def test_assert_url_matches_view_class(self):
        self.assert_url_matches_view(
            view=views.MyView,
            expected_url='/foo/',
            url_name='class-view',
        )

    def test_assert_url_matches_view_rest_framework(self):
        self.assert_url_matches_view(
            view=views.MyAPIView,
            expected_url='/bar/',
            url_name='api-view',
        )

    def test_assert_url_matches_view_missing_as_view(self):
        with pytest.raises(AssertionError):
            self.assert_url_matches_view(
                view=views.MyAPIView,
                expected_url='/spam/',
                url_name='missing-as-view',
            )

    def test_assert_url_matches_view_same_name(self):
        with pytest.raises(AssertionError):
            self.assert_url_matches_view(
                view=other_views.my_view,
                expected_url='/',
                url_name='function-view',
            )
