import mock
from incuna_test_utils.testcases.integration import BaseAdminIntegrationTestCase
from tests.factories import UserFactory
from tests.models import User


class AdminIntegrationTestCase(BaseAdminIntegrationTestCase):
    user_factory = UserFactory
    model = User

    def setUp(self):
        super(AdminIntegrationTestCase, self).setUp()
        self.client.get = mock.MagicMock()

    def test_get_url_name(self):
        action = 'cleaning'
        url_name = self.get_url_name(action)
        expected = 'admin:tests_user_cleaning'

        self.assertEqual(url_name, expected)

    def test_get_admin_add_page(self):
        self.get_admin_add_page()
        self.client.get.assert_called_with('/admin/tests/user/add/')

    def test_get_admin_changelist_page(self):
        self.get_admin_changelist_page()
        self.client.get.assert_called_with('/admin/tests/user/')

    def test_get_admin_change_page(self):
        user = self.user_factory.create()

        self.get_admin_change_page(user)
        expected = '/admin/tests/user/{}/'.format(user.pk)
        self.client.get.assert_called_with(expected)

    def test_get_admin_delete_page(self):
        user = self.user_factory.create()

        self.get_admin_delete_page(user)
        expected = '/admin/tests/user/{}/delete/'.format(user.pk)
        self.client.get.assert_called_with(expected)
