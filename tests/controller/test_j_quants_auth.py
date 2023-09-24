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
    
    def test_init(self):
        """JQuantsApiIDTokenControllerの初期化（__init__()）テスト
        """
        with self.subTest('refresh_token_fetcherの初期化'):
            self.assertIsInstance(
                self.j_quants_api_id_token_controller.refresh_token_fetcher,
                IRefreshTokenFetcher,
            )
        
        with self.subTest('id_token_fetcherの初期化'):
            self.assertIsInstance(
                self.j_quants_api_id_token_controller.id_token_fetcher,
                IIDTokenFetcher,
            )
