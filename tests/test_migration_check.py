from django.core.management import call_command, CommandError
from django.test import modify_settings, TestCase


class TestPartialMigrationCheck(TestCase):
    @modify_settings(INSTALLED_APPS={'prepend': 'tests.complete_migrations'})
    def test_complete_migrations_pass_check(self):
        """An app with up to date migrations passes the check."""
        self.assertIsNone(call_command('check_migrations'))

    @modify_settings(INSTALLED_APPS={'prepend': 'tests.partial_migrations'})
    def test_partial_migrations_fail_check(self):
        """An app with incomplete migration files fails the check."""
        message = (
            "Your models have changes that are not yet reflected " +
            "in a migration. Run 'manage.py makemigrations' to make " +
            "new migrations."
        )

        with self.assertRaisesMessage(CommandError, message):
            call_command('check_migrations')
