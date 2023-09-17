from usecase import (
  IRefreshTokenFetcher,
  IIDTokenFetcher,
  RefreshTokenFetchOutput,
  IDTokenFetchOutput,
)
import RESPONSE_OK

class JQuantsApiIDTokenController():
  refresh_token_fetcher: IRefreshTokenFetcher
  id_token_fetcher: IIDTokenFetcher
  
  def __init__(
    self,
    refresh_token_fetcher: IRefreshTokenFetcher,
    id_token_fetcher: IIDTokenFetcher,
  ):

      self.refresh_token_fetcher: IRefreshTokenFetcher = refresh_token_fetcher
      self.id_token_fetcher: IIDTokenFetcher = id_token_fetcher

  def get_id_token(self):
    if not self.id_token_fetcher.refresh_token:
        # TODO: id_token_fetcher側に、refresh_tokenの定義がないのでつける
        # refresh_tokenをまだ所持していない場合
        refresh_token_fetcher_output: RefreshTokenFetchOutput = self.refresh_token_fetcher.fetch()

    if refresh_token_fetcher_output.response_code == RESPONSE_OK:
        # TODO: id_token_fetcher.refresh_tokenは、fetch()内で、初期化したい
        self.id_token_fetcher.refresh_token = refresh_token_fetcher_output.token
        # TODO: リフレッシュトークンが取得できなかった（response_code != RESPONSE_OK）のエラー処理

    id_token_fetcher_output: IDTokenFetchOutput = self.id_token_fetcher.fetch()
    if id_token_fetcher_output.response_code == RESPONSE_OK:
        return self.id_token_fetcher_output.token
        # TODO: IDトークンが取得できなかった（response_code != RESPONSE_OK）のエラー処理
