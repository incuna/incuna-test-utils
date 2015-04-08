from feincms.module.page.models import Page

from incuna_test_utils.factories.feincms_page import PageFactory


def test_pagefactory():
    page = PageFactory.build()
    assert isinstance(page, Page)
    assert 'Page' in page.title
    assert 'page' in page.slug
