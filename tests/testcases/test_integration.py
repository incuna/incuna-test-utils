from django.contrib.sessions.backends.base import SessionBase
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
import pytest

from incuna_test_utils.testcases.integration import BaseIntegrationTestCase
from tests.factories import UserFactory


def view(request, *args, **kwargs):
    return HttpResponse('')


class IntegrationTestCase(BaseIntegrationTestCase):
    user_factory = UserFactory
    view = view

    def test_access_view(self):
        response = self.access_view()
        assert isinstance(response, HttpResponse)

        request = response.request
        assert isinstance(request, WSGIRequest)
        assert isinstance(request.session, SessionBase)

    def test_access_view_request(self):
        request = self.create_request()
        response = self.access_view(request=request)

        assert response.request == request

        with pytest.raises(AttributeError):
            response.request.session

    def test_assert_count(self):
        haystack = [1, 1, 3, 1, 2, 4]
        needle = 1
        count = 3
        self.assert_count(needle, haystack, count)

    def test_assert_count_fail(self):
        haystack = [1, 1, 3, 1, 2, 4]
        needle = 1
        count = 4

        with pytest.raises(AssertionError):
            self.assert_count(needle, haystack, count)
