from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.db import connections, DEFAULT_DB_ALIAS
from django.db.migrations.autodetector import MigrationAutodetector
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.state import ProjectState


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Detect model changes without migrations.

        The implementation here is a very stripped down version of the
        `migrate` management command in django core.
        """
        connection = connections[DEFAULT_DB_ALIAS]
        executor = MigrationExecutor(connection)
        autodetector = MigrationAutodetector(
            executor.loader.project_state(),
            ProjectState.from_apps(apps),
        )
        changes = autodetector.changes(graph=executor.loader.graph)
        if changes:
            message = (
                "Your models have changes that are not yet reflected " +
                "in a migration. Run 'manage.py makemigrations' to make " +
                "new migrations."
            )
            raise CommandError(message)
