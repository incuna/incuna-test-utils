from django.db.models.base import ModelBase


class AbstractModelMixin(object):
    """
    Mixin class for tests of model mixins. To use, subclass and specify
    the mixin class variable. A model using the mixin will be made
    available in self.model.

    From http://michael.mior.ca/2012/01/14/unit-testing-django-model-mixins/
    via http://stackoverflow.com/a/9678200/400691, modified as we don't need an
    object in the database.
    """
    def setUp(self):
        # Create a dummy model which extends the mixin
        self._model_name = '__TestModel__' + self.mixin.__name__
        self.model = ModelBase(
            self._model_name,
            (self.mixin,),
            {'__module__': self.mixin.__module__},
        )
