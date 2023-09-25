# TODO: IRefreshTokenFetcherに、属性を持たせないようにする。

from ..usecase import (
  IRefreshTokenFetcher,
  IIDTokenFetcher,
  RefreshTokenFetchOutput,
  IDTokenFetchOutput,
)
from ..constants import RESPONSE_OK

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

  def get_id_token(
      self,
      mail_address: str,
      password: str,
  ):
    refresh_token_fetcher_output: RefreshTokenFetchOutput = self.refresh_token_fetcher.fetch(
       mail_address,
       password,
    )

    if refresh_token_fetcher_output.response_code == RESPONSE_OK:
      # TODO: リフレッシュトークンが取得できなかった（response_code != RESPONSE_OK）のエラー処理
      id_token_fetcher_output: IDTokenFetchOutput = self.id_token_fetcher.fetch(
        refresh_token_fetcher_output.token
      )
    if id_token_fetcher_output.response_code == RESPONSE_OK:
      # TODO: IDトークンが取得できなかった（response_code != RESPONSE_OK）のエラー処理
      return id_token_fetcher_output.token
