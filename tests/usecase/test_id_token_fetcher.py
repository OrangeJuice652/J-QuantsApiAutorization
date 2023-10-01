import requests, unittest
from unittest.mock import patch, Mock
from src.j_quants_auth.usecase import IDTokenFetcher, IDTokenFetchOutput
from src.j_quants_auth.constants import RESPONSE_OK

class TestIDTokenFetcher(unittest.TestCase):
    def setUp(self):
        self.id_token_fetcher = IDTokenFetcher()
    
    def test_fetch_200(self):
        """fetch()のテスト(response_code == 200の場合)
        """
        with patch('requests.post') as mock:
            response = requests.models.Response()
            response.status_code = RESPONSE_OK
            response.json = Mock(return_value={'idToken': 'id_token'})
            mock.return_value = response
            result: IDTokenFetchOutput = self.id_token_fetcher.fetch('refresh_token')

            with self.subTest('response_code == 200'):
                self.assertEqual(
                    result.response_code,
                    RESPONSE_OK,
                )

            with self.subTest('tokenの取得'):
                self.assertEqual(
                    result.token,
                    'id_token',
                )
