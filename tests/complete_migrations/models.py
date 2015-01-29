from django.db import models


class Stub(models.Model):
    """
    A stub model for testing check_migrations.

    Has a complete set of migrations.
    """
    name = models.CharField(max_length=255)
