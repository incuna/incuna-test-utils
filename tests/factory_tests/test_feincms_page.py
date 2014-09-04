from feincms.module.page.models import Page
import pytest

from incuna_test_utils.factories.feincms_page import PageFactory


@pytest.mark.django_db
def test_pagefactory():
    page = PageFactory.build()
    assert isinstance(page, Page)
    assert 'Page' in page.title
    assert 'page' in page.slug
