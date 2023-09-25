import requests, unittest
from unittest.mock import patch, Mock
from j_quants_auth.usecase import RefreshTokenFetcher, RefreshTokenFetchOutput
from j_quants_auth.constants import RESPONSE_OK

class TestRefreshTokenFetcher(unittest.TestCase):
    def setUp(self):
        self.refresh_token_fetcher = RefreshTokenFetcher()
    
    def test_fetch_200(self):
        """fetch()のテスト(response_code == 200の場合)
        """
        with patch('requests.post') as mock:
            response = requests.models.Response()
            response.status_code = RESPONSE_OK
            response.json = Mock(return_value={'refreshToken': 'refresh_token'})
            mock.return_value = response
            result: RefreshTokenFetchOutput = self.refresh_token_fetcher.fetch(
                'mail_address',
                'password',
            )

            with self.subTest('response_code == 200'):
                self.assertEqual(
                    result.response_code,
                    RESPONSE_OK,
                )

            with self.subTest('tokenの取得'):
                self.assertEqual(
                    result.token,
                    'refresh_token',
                )
