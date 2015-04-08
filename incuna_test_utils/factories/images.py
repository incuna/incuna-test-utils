from io import BytesIO

import factory
from PIL import Image

from ..utils import TEST_SERVER


def simple_png():
    """Create a 1x1 black png in memory and return a handle to it."""
    image_file = BytesIO()
    image = Image.new('RGBA', (1, 1))
    image.save(image_file, 'png')
    image_file.name = 'test.png'
    image_file.url = '{0}/{1}'.format(
        TEST_SERVER,
        image_file.name,
    )
    image_file._committed = True
    image_file.seek(0)
    return image_file


class LocalFileField(factory.django.FileField):
    """
    A factory file field class that reads an image from disk.

    Suitable for using as a FileField or ImageField.

        class ATestFactory(factory.Factory):
            file = LocalFileField()
    """
    def __init__(self, *args, **kwargs):
        defaults = {
            'from_path': 'incuna_test_utils/factories/images/image.png',
        }
        defaults.update(kwargs)
        super(LocalFileField, self).__init__(*args, **defaults)


class SimplePngFileField(factory.LazyAttribute):
    """
    A factory file field class that creates an image in memory.

    Suitable for using as a FileField or ImageField.

        class ATestFactory(factory.Factory):
            file = SimplePngFileField()
    """
    def __init__(self, method=None, *args, **kwargs):
        if not method:
            def png(a):
                return simple_png()
            method = png
        super(SimplePngFileField, self).__init__(method, *args, **kwargs)


def uploadable_file():
    """
    Return an object that can be uploaded to a FileField via a Django form.

    Uploading files in a form in a test can be a pain. This method returns a file object
    that can be easily uploaded via request.FILES.

    Example usage:

        file_data = {
            'file_field_name': uploadable_file(),
        }
        form = form_class_being_tested(files=file_data)

    Note that the form_class_being_tested is instantiated using the `files` kwarg and not
    `data`.  The two are not mutually exclusive, but the file being uploaded must be
    passed in using `files`, which correlates to `request.FILES`. Other form data can be
    passed in using `data` as normal.
    """
    return open('incuna_test_utils/factories/images/image.png', mode='rb')
