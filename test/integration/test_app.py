import json
from unittest import TestCase

from chalice.config import Config
from chalice.local import LocalGateway

from app import app


class TestApp(TestCase):
    def setUp(self):
        self.lg = LocalGateway(app, Config())

    def test_get_books(self):
        response = self.lg.handle_request(method='GET',
                                          path='/books',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == [
            dict(book_id=1),
            dict(book_id=2)
        ]

    def test_post_book(self):
        body = dict(book_info='hello')
        response = self.lg.handle_request(method='POST',
                                          path='/books',
                                          headers={
                                              'Content-Type': 'application/json'
                                          },
                                          body=json.dumps(body))

        assert response['statusCode'] == 201
        assert response['headers'].get('Location') == '/books/3'

    def test_get_book_by_id(self):
        response = self.lg.handle_request(method='GET',
                                          path='/books/4',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(book_id=4)

    def test_put_book_by_id(self):
        body = dict(book_info='hello')
        response = self.lg.handle_request(method='PUT',
                                          path='/books/4',
                                          headers={},
                                          body=json.dumps(body))

        assert response['statusCode'] == 204
        assert json.loads(response['body']) is None

    def test_delete_book_by_id(self):
        response = self.lg.handle_request(method='DELETE',
                                          path='/books/4',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 204
        assert json.loads(response['body']) is None
