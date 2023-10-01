import unittest
from unittest.mock import Mock
from src.j_quants_auth.constants import RESPONSE_OK, RESPONSE_FORBIDDEN
from src.j_quants_auth.controller import JQuantsApiIDTokenController
from src.j_quants_auth.usecase import (
    RefreshTokenFetcher,
    IDTokenFetcher,
    RefreshTokenException,
    IDTokenFetcherException,
)
from ..mocks.usecase.fetcher_output import (
    MockTokenOutput,
)


class TestJQuantsApiIDTokenController(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_fetch_200(self):
        """get_id_token()のテスト
        refresh_token_fetcher -> response_code == 200
        id_token_fetcher -> response_code == 200
        """
        mock_refresh_token_fetcher = RefreshTokenFetcher()
        mock_refresh_token_fetcher.fetch = Mock(
            return_value=MockTokenOutput(
                RESPONSE_OK,
                '',
                'test_refresh_token',
            )
        )

        mock_id_token_fetcher = IDTokenFetcher()
        mock_id_token_fetcher.fetch = Mock(
            return_value=MockTokenOutput(
                RESPONSE_OK,
                '',
                'test_id_token',
            )
        )
        
        j_quants_api_id_token_controller = JQuantsApiIDTokenController(
            mock_refresh_token_fetcher,
            mock_id_token_fetcher,
        )
        test_id_token = j_quants_api_id_token_controller.get_id_token('', '')
        self.assertEqual(test_id_token, 'test_id_token')
    
    def test_fetch_raise_exception(self):
        """get_id_tokenのテスト
        パターン1
        refresh_token_fetcher -> response_code == 403
        id_token_fetcher -> response_code == 200
        パターン2
        refresh_token_fetcher -> response_code == 200
        id_token_fetcher -> response_code == 403
        """
        with self.subTest('パターン1'):
            with self.assertRaises(RefreshTokenException):
                mock_refresh_token_fetcher = RefreshTokenFetcher()
                mock_refresh_token_fetcher.fetch = Mock(
                    return_value=MockTokenOutput(
                        RESPONSE_FORBIDDEN,
                        'Missing Authentication Token. The method or resources may not be supported.',
                        '',
                    )
                )

                mock_id_token_fetcher = IDTokenFetcher()
                mock_id_token_fetcher.fetch = Mock(
                    return_value=MockTokenOutput(
                        RESPONSE_OK,
                        '',
                        'test_id_token',
                    )
                )
                
                j_quants_api_id_token_controller = JQuantsApiIDTokenController(
                    mock_refresh_token_fetcher,
                    mock_id_token_fetcher,
                )
                j_quants_api_id_token_controller.get_id_token('', '')
        
        with self.subTest('パターン2'):
            with self.assertRaises(IDTokenFetcherException):
                mock_refresh_token_fetcher = RefreshTokenFetcher()
                mock_refresh_token_fetcher.fetch = Mock(
                    return_value=MockTokenOutput(
                        RESPONSE_OK,
                        '',
                        'test_refresh_token',
                    )
                )

                mock_id_token_fetcher = IDTokenFetcher()
                mock_id_token_fetcher.fetch = Mock(
                    return_value=MockTokenOutput(
                        RESPONSE_FORBIDDEN,
                        'Missing Authentication Token. The method or resources may not be supported.',
                        'test_id_token',
                    )
                )
                
                j_quants_api_id_token_controller = JQuantsApiIDTokenController(
                    mock_refresh_token_fetcher,
                    mock_id_token_fetcher,
                )
                j_quants_api_id_token_controller.get_id_token('', '')
