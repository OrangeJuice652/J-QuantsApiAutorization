import unittest
from j_quants_auth import JQuantsApiIDTokenController
from j_quants_auth.usecase import IIDTokenFetcher, IRefreshTokenFetcher

class MockIDTokenFetcher(IIDTokenFetcher):
    pass


class MockRefreshTokenFetcher(IRefreshTokenFetcher):
    pass


class TestJQuantsApiIDTokenController(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_fetch_200(self):
        mock_refresh_token_fetcher = MockRefreshTokenFetcher()
        mock_refresh_token_output = MockRefreshTokenOutput(RESPONSE_200, 'test_refresh_token')
        mock_refresh_token.fetch = Mock(result_value=mock_refresh_token)

        mock_id_token_fetcher = MockIDTokenFetcher()
        mock_id_token_output = MockIDTokenOutput(RESPONSE_200, 'test_id_token')
        mock_id_token.fetch = Mock(result_value=mock_id_token)
        
        j_quants_api_id_token_controller = JQuantsApiIDTokenController(
            MockRefreshTokenFetcher(),
            MockIDTokenFetcher(),
        )
        test_id_token = j_quants_api_id_token_controller.get_id_token
        self.assertEqual(test_id_token, 'tests_id_token')
