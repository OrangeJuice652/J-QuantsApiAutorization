from dataclasses import dataclass

RESPONSE_OK = '200'
RESPONSE_BAD_REQUEST = '400'
RESPONSE_FORBIDDEN = '403'
RESPONSE_INTERNAL_SERVER_ERROR = '500'

class JQuantsApiIDTokenController():
  refresh_token_fetcher: IRefreshTockenFetcher
  id_token_fetcher: IIDTockenFetcher
  
  def __init__(
    self,
    refresh_token_fetcher: IRefreshTockenFetcher,
    id_token_fetcher: IIDTockenFetcher):

      self.refresh_token_fetcher = refresh_token_fetcher
      self.id_token_fetcher = id_token_fetcher

  def get_id_token():
        if not self.id_token_fetcher.refresh_token:
            # refresh_tokenをまだ所持していない場合
            refresh_token_fetcher_output: FetcherOutput = self.refresh_token_fetcher.fetch()

        if refresh_token_fetcher_output.response_code == RESPONSE_OK:
            self.id_token_fetcher.refresh_token = refresh_token_fetcher_output.token
            # TODO: リフレッシュトークンが取得できなかった（response_code != RESPONSE_OK）のエラー処理

    id_token_fetcher_output: FetcherOutput = self.id_token_fetcher.fetch()
    if id_token_fetcher_output.response_code == RESPONSE_OK:
        return self.id_token_fetcher_output.token
        # TODO: IDトークンが取得できなかった（response_code != RESPONSE_OK）のエラー処理

@dataclass
class TokenFetcherOutput():
    response_code: str
    response_message: str
    token: str

from abc import ABC, abstractmethod
import requests
import json

JQUANTS_API_URI = 'https://api.jquants.com/v1' 
REFRESH_TOKEN_URL = '/token/auth_user'

class IRefreshTockenFetcher(ABC):
    @abstractmethod
    def __init__(
        self,
        mail_address: str,
        password: str,
    ):
        pass

    @abstractmethod
    def fetch() -> TokenFetcherOutput:
        pass

class RefreshTokenFetcher(IRefreshTokenFetcher):
    def __init__(
        self,
        mail_address: str,
        password: str,
    ):
        self.mail_address = mail_address
        self.password = password

    def fetch() -> TokenFetcherOutput:
        request_body = {
            'mailaddress': self.mail_address,
            'password': self.password,
        }
        response = requests.post(
            JQUANTS_API_URI+REFRESH_TOKEN_URL,
            data=json.dumps(request_body),
        )
        return TokenFetcherOutput(response)



















