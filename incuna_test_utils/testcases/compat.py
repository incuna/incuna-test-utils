class Python2CountEqualMixin(object):
    """Add assertCountEqual to python 2 TestCase"""
    def __init__(self, *args, **kwargs):
        super(Python2CountEqualMixin, self).__init__(*args, **kwargs)
        if not hasattr(self, 'assertCountEqual'):
            self.assertCountEqual = self.assertItemsEqual
