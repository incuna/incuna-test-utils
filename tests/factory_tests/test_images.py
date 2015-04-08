from io import BufferedReader, BytesIO

import factory
from django.core.files import File

from incuna_test_utils.factories import images


def test_local_file_field():
    class FileFactory(factory.StubFactory):
        file = images.LocalFileField()

    file = FileFactory.build().file
    assert isinstance(file, File)
    assert isinstance(file.file, BufferedReader)


def test_simple_png_file_field():
    class FileFactory(factory.StubFactory):
        image = images.SimplePngFileField()

    image = FileFactory.build().image
    assert isinstance(image, BytesIO)


def test_uploadable_file():
    file = images.uploadable_file()
    assert isinstance(file, BufferedReader)
