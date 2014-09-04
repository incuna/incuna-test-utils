from django.contrib.auth.models import AnonymousUser, User
from django.contrib import messages
from django.contrib.sessions.backends.base import SessionBase
from django.core.exceptions import ImproperlyConfigured

from incuna_test_utils.testcases.request import (
    BaseRequestTestCase,
    DummyStorage,
)
from tests.factories import UserFactory


class RequestTestCase(BaseRequestTestCase):
    user_factory = UserFactory

    def test_create_request(self):
        request = self.create_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, '/')
        self.assertIsInstance(request.user, User)
        self.assertIsInstance(request._messages, DummyStorage)

    def test_create_request_post(self):
        request = self.create_request('post')
        self.assertEqual(request.method, 'POST')

    def test_create_request_url(self):
        url = '/foo/'
        request = self.create_request(url=url)
        self.assertEqual(request.path, url)

    def test_create_request_user(self):
        user = UserFactory.build()
        request = self.create_request(user=user)
        self.assertEqual(request.user, user)

    def test_create_request_anonymous(self):
        request = self.create_request(auth=False)
        self.assertIsInstance(request.user, AnonymousUser)

    def test_create_request_data(self):
        data = {'foo': 'bar'}
        request = self.create_request(data=data)
        self.assertEqual(request.DATA, data)

    def test_create_user(self):
        user = self.create_user()
        self.assertIsInstance(user, User)

    def test_create_user_anonymous(self):
        user = self.create_user(auth=False)
        self.assertIsInstance(user, AnonymousUser)

    def test_add_session_to_request(self):
        request = self.create_request()
        self.add_session_to_request(request)
        self.assertIsInstance(request.session, SessionBase)

    def test_get_view(self):
        with self.assertRaises(ImproperlyConfigured):
            self.get_view()


def function_view(request):
    return request


class RequestTestCaseFunctionView(BaseRequestTestCase):
    view = function_view

    def test_get_view(self):
        view = self.get_view()
        self.assertEqual(view, function_view)


class ClassView:
    @classmethod
    def as_view(cls):
        return function_view


class RequestTestCaseClassView(BaseRequestTestCase):
    view = ClassView

    def test_get_view(self):
        view = self.get_view()
        self.assertEqual(view, function_view)


class TestDummyStorage:
    def test_add(self):
        message_storage = DummyStorage()

        message = "I've added a message!"
        message_storage.add(messages.INFO, message)

        assert message in message_storage.store

    def test_iter(self):
        message_storage = DummyStorage()
        message = "A message!"
        message_storage.store = [message]

        assert message in iter(message_storage)
