from rest_framework.test import APIRequestFactory, force_authenticate

from .api_examples import APIExampleMixin
from .request import BaseRequestTestCase


class BaseAPIRequestTestCase(BaseRequestTestCase):
    """
    Extend BaseRequestTestCase with REST framework compatibility.

    Must be subclassed with an user_factory attribute in order to work.
    """
    request_factory = APIRequestFactory

    def create_request(self, method='get', url='/', user=None, auth=True, **kwargs):
        kwargs['format'] = 'json'
        request = super(BaseAPIRequestTestCase, self).create_request(
            method=method,
            url=url,
            user=user,
            auth=auth,
            **kwargs)
        if auth:
            force_authenticate(request, request.user)
        return request


class BaseAPIExampleTestCase(APIExampleMixin, BaseAPIRequestTestCase):
    SERVER_NAME = 'localhost:8000'

    def create_request(self, *args, **kwargs):
        """Set the server domain name on the new request."""
        return super(BaseAPIExampleTestCase, self).create_request(
            *args, SERVER_NAME=self.SERVER_NAME, **kwargs)
