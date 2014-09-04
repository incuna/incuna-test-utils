from django.contrib.sessions.backends.base import SessionBase
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from incuna_test_utils.testcases.integration import BaseIntegrationTestCase
from tests.factories import UserFactory


def view(request, *args, **kwargs):
    return HttpResponse('')


class IntegrationTestCase(BaseIntegrationTestCase):
    user_factory = UserFactory
    view = view

    def test_access_view(self):
        response = self.access_view()
        self.assertIsInstance(response, HttpResponse)

        request = response.request
        self.assertIsInstance(request, WSGIRequest)
        self.assertIsInstance(request.session, SessionBase)

    def test_access_view_request(self):
        request = self.create_request()
        response = self.access_view(request=request)

        self.assertEqual(response.request, request)

        with self.assertRaises(AttributeError):
            response.request.session
