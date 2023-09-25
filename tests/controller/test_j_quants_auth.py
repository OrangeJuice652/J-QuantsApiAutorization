import unittest
from j_quants_auth import JQuantsApiIDTokenController
from j_quants_auth.usecase import IIDTokenFetcher, IRefreshTokenFetcher

class MockIDTokenFetcher(IIDTokenFetcher):
    pass


class MockRefreshTokenFetcher(IRefreshTokenFetcher):
    pass


class TestJQuantsApiIDTokenController(unittest.TestCase):
    def setUp(self):
        self.j_quants_api_id_token_controller = JQuantsApiIDTokenController(
            MockRefreshTokenFetcher(),
            MockIDTokenFetcher(),
        )
    
    def fetch(self):
        self.j_quants_api_id_token_controller.get_id_token(
            'mail_address',
            'password',
        )
