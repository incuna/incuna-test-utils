from django.contrib.auth.models import AnonymousUser, User

from incuna_test_utils.testcases.request import BaseRequestTestCase
from tests.factories import UserFactory


class RequestTestCase(BaseRequestTestCase):
    user_factory = UserFactory

    def test_create_request(self):
        request = self.create_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, '/')
        self.assertIsInstance(request.user, User)

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

    def test_create_user(self):
        user = self.create_user()
        self.assertIsInstance(user, User)

    def test_create_user_anonymous(self):
        user = self.create_user(auth=False)
        self.assertIsInstance(user, AnonymousUser)
