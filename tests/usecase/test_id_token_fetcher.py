import requests, unittest
from unittest.mock import patch, Mock
from j_quants_auth.usecase import IDTokenFetcher, IDTokenFetchOutput
from j_quants_auth.constants import RESPONSE_OK

class TestIDTokenFetcher(unittest.TestCase):
    def setUp(self):
        self.id_token_fetcher = IDTokenFetcher(
            'test_id_token',
        )

    def test_init(self):
        """IDTokenFetcherの初期化テスト
        """
        with self.subTest('リフレッシュトークンの初期化（引数指定なし）'):
            no_refresh_token_id_token_fetcher = IDTokenFetcher()
            self.assertEqual(
                no_refresh_token_id_token_fetcher.refresh_token,
                None,
            )

        with self.subTest('リフレッシュトークンの初期化（引数指定）'):
            self.assertEqual(
                self.id_token_fetcher.refresh_token,
                'test_id_token',
            )
        
    
    def test_fetch_200(self):
        """fetch()のテスト(response_code == 200の場合)
        """
        with patch('requests.post') as mock:
            response = requests.models.Response()
            response.status_code = RESPONSE_OK
            response.json = Mock(return_value={'idToken': 'test_id_token'})
            mock.return_value = response
            result: IDTokenFetchOutput = self.id_token_fetcher.fetch()

            with self.subTest('response_code == 200'):
                self.assertEqual(
                    result.response_code,
                    RESPONSE_OK,
                )

            with self.subTest('tokenの取得'):
                self.assertEqual(
                    result.token,
                    'test_id_token',
                )
