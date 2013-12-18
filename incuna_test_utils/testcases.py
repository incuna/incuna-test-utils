from django.db.models.base import ModelBase
from django.test import TestCase


class AbstractModelTestCase(TestCase):
    """
Base class for tests of model mixins. To use, subclass and specify
the mixin class variable. A model using the mixin will be made
available in self.model.

From http://michael.mior.ca/2012/01/14/unit-testing-django-model-mixins/
via http://stackoverflow.com/a/9678200/400691, modified as we don't need an
object in the database.
"""
    def setUp(self):
        # Create a dummy model which extends the mixin
        self.model = ModelBase(
            '__TestModel__' + self.mixin.__name__,
            (self.mixin,),
            {'__module__': self.mixin.__module__},
        )
