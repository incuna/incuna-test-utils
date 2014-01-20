from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from ..factories.user import UserFactory


class RequestTestCase(TestCase):
    user_factory = UserFactory
    request_factory = RequestFactory

    def create_request(self, method='get', url='/', user=None, auth=True, **kwargs):
        if user is None:
            user = self.create_user(auth=auth)
        request = getattr(self.request_factory(), method)(url, **kwargs)
        request.user = user
        if 'data' in kwargs:
            request.DATA = kwargs['data']
        return request

    def create_user(self, auth=True, **kwargs):
        if auth:
            return self.user_factory.create(**kwargs)
        else:
            return AnonymousUser()
