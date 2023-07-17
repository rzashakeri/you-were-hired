"""tests for page app"""
from .fixtures import page_name, page_slug
from ..models import PageModel


class TestPageModel:
    """test for the page model"""

    def test_str_method(self):
        """test for str method"""

        page = PageModel(name=page_name, slug=page_slug)
        assert str(page) == page_name
