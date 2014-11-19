import pytest
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.sessions.backends.base import SessionBase
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View

from incuna_test_utils.testcases.request import (
    BaseRequestTestCase,
    DummyStorage,
)
from tests.factories import UserFactory


class RequestTestCase(BaseRequestTestCase):
    user_factory = UserFactory

    def test_create_request(self):
        request = self.create_request()
        assert request.method == 'GET'
        assert request.path == '/'
        assert isinstance(request.user, User)
        assert isinstance(request._messages, DummyStorage)

    def test_create_request_post(self):
        request = self.create_request('post')
        assert request.method == 'POST'

    def test_create_request_url(self):
        url = '/foo/'
        request = self.create_request(url=url)
        assert request.path == url

    def test_create_request_user(self):
        user = UserFactory.build()
        request = self.create_request(user=user)
        assert request.user == user

    def test_create_request_anonymous(self):
        request = self.create_request(auth=False)
        assert isinstance(request.user, AnonymousUser)

    def test_create_request_data(self):
        data = {'foo': 'bar'}
        request = self.create_request(data=data)
        assert request.DATA == data

    def test_create_user(self):
        user = self.create_user()
        assert isinstance(user, User)

    def test_create_user_anonymous(self):
        user = self.create_user(auth=False)
        assert isinstance(user, AnonymousUser)

    def test_add_session_to_request(self):
        request = self.create_request()
        self.add_session_to_request(request)
        assert isinstance(request.session, SessionBase)

    def test_get_view(self):
        with pytest.raises(ImproperlyConfigured):
            self.get_view()

    def test_view_instance(self):
        """
        Check view_instance raises ImproperlyConfigured if view is not set.
        """
        with pytest.raises(ImproperlyConfigured):
            self.view_instance()


def function_view(request):
    return request


class RequestTestCaseFunctionView(BaseRequestTestCase):
    view = function_view

    def test_get_view(self):
        view = self.get_view()
        assert view == function_view


class ClassView(View):
    @classmethod
    def as_view(cls):
        return function_view


class RequestTestCaseClassView(BaseRequestTestCase):
    view = ClassView

    def test_get_view(self):
        view = self.get_view()
        assert view == function_view

    def test_view_instance(self):
        """
        Check view_instance adds request, args and kwargs to a view instance.
        """
        request = object()
        args = (object(),)
        kwargs = {'mock': object()}

        view = self.view_instance(request, *args, **kwargs)

        assert isinstance(view, self.view)
        assert view.request == request
        assert view.args == args
        assert view.kwargs == kwargs


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
