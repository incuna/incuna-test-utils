from io import BufferedReader, BytesIO

import factory
import pytest
from django.core.files import File

from incuna_test_utils.factories import images


@pytest.mark.django_db
def test_local_file_field():
    class FileFactory(factory.StubFactory):
        file = images.LocalFileField()

    file = FileFactory.build().file
    assert isinstance(file, File)
    assert isinstance(file.file, BufferedReader)


@pytest.mark.django_db
def test_simple_png_file_field():
    class FileFactory(factory.StubFactory):
        image = images.SimplePngFileField()

    image = FileFactory.build().image
    assert isinstance(image, BytesIO)


@pytest.mark.django_db
def test_uploadable_file():
    file = images.uploadable_file()
    assert isinstance(file, BufferedReader)
