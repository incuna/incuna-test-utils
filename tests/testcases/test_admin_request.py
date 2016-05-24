from unittest import skipIf, skipUnless

import mock

from incuna_test_utils.compat import DJANGO_GTE_19
from incuna_test_utils.testcases.integration import BaseAdminIntegrationTestCase
from tests.factories import AdminFactory
from tests.models import User


class AdminIntegrationTestCase(BaseAdminIntegrationTestCase):
    user_factory = AdminFactory
    model = User

    def setUp(self):
        """Mock the client to test what it gets called with."""
        super(AdminIntegrationTestCase, self).setUp()
        self.client.get = mock.MagicMock()

    def test_get_url_name(self):
        """Assert url name generated is correct."""
        action = 'cleaning'
        url_name = self.get_url_name(action)
        expected = 'admin:tests_user_cleaning'

        self.assertEqual(url_name, expected)

    def test_get_admin_add_page(self):
        """Assert the right page is called when adding a record."""
        self.get_admin_add_page()
        self.client.get.assert_called_with('/admin/tests/user/add/')

    def test_get_admin_changelist_page(self):
        """Assert the right page is called when listing records."""
        self.get_admin_changelist_page()
        self.client.get.assert_called_with('/admin/tests/user/')

    @skipIf(DJANGO_GTE_19, "Django 1.9 has updated the admin url.")
    def test_get_admin_change_page_django_lte_19(self):
        """Assert the right page is called when changing a record."""
        user = self.user_factory.create()

        self.get_admin_change_page(user)
        expected = '/admin/tests/user/{}/'.format(user.pk)
        self.client.get.assert_called_with(expected)

    @skipUnless(DJANGO_GTE_19, "Django 1.9 has updated the admin url.")
    def test_get_admin_change_page(self):
        """Assert the right page is called when changing a record."""
        user = self.user_factory.create()

        self.get_admin_change_page(user)
        expected = '/admin/tests/user/{}/change/'.format(user.pk)
        self.client.get.assert_called_with(expected)

    def test_get_admin_delete_page(self):
        """Assert the right page is called when deleting a record."""
        user = self.user_factory.create()

        self.get_admin_delete_page(user)
        expected = '/admin/tests/user/{}/delete/'.format(user.pk)
        self.client.get.assert_called_with(expected)
