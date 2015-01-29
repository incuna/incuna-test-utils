from django.db import models


class Stub(models.Model):
    """
    A stub model for testing check_migrations.

    Has an incomplete set of migrations: the `age field is missing.
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
