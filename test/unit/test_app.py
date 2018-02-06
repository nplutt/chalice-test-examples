from unittest import TestCase
import app


class TestApp(TestCase):

    def test_get_book(self):
        assert app.get_book('1') == dict(book_id=1)
