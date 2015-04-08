from io import BufferedReader, BytesIO

import factory
from django.core.files import File

from incuna_test_utils.factories import images


# In Python 2 Django's File wraps the builtin `file`, but that doesn't exist in Python 3.
try:
    FILE_TYPE = file
except NameError:
    FILE_TYPE = BufferedReader


def test_local_file_field():
    class FileFactory(factory.StubFactory):
        image = images.LocalFileField()

    built_file = FileFactory.build().image
    assert isinstance(built_file, File)
    assert isinstance(built_file.file, FILE_TYPE)


def test_simple_png_file_field():
    class FileFactory(factory.StubFactory):
        image = images.SimplePngFileField()

    built_file = FileFactory.build().image
    assert isinstance(built_file, File)
    assert isinstance(built_file.file, BytesIO)


def test_uploadable_file():
    built_file = images.uploadable_file()
    assert isinstance(built_file, File)
    assert isinstance(built_file.file, FILE_TYPE)
