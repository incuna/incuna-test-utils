from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory


class DummyStorage:
    def __init__(self):
        self.store = list()

    def add(self, level, message, extra_tags=''):
        self.store.add(message)

    def __iter__(self):
        for item in self.store:
            yield item


class BaseRequestTestCase(TestCase):
    """
    Extend django.test.TestCase with a create_request method.

    BaseRequestTestCase must be subclassed with a user_factory attribute to
    create a default user for the request.
    """
    request_factory = RequestFactory

    def create_request(self, method='get', url='/', user=None, auth=True, **kwargs):
        if user is None:
            user = self.create_user(auth=auth)
        request = getattr(self.request_factory(), method)(url, **kwargs)
        request.user = user

        if 'data' in kwargs:
            request.DATA = kwargs['data']

        if 'messages' in kwargs:
            request._messages = kwargs['messages']
        else:
            request._messages = DummyStorage()

        return request

    def create_user(self, auth=True, **kwargs):
        if auth:
            return self.user_factory.create(**kwargs)
        else:
            return AnonymousUser()
