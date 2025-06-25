# TODO: IRefreshTokenFetcherに、属性を持たせないようにする。
import os
from ..usecase import (
  IRefreshTokenFetcher,
  IIDTokenFetcher,
  RefreshTokenFetchOutput,
  IDTokenFetchOutput,
  RefreshTokenException,
  IDTokenFetcherException,
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
      self._id_token = None

  @property
  def id_token(self):
      if self._id_token is None:
        refresh_token_fetcher_output: RefreshTokenFetchOutput = self.refresh_token_fetcher.fetch(
           os.getenv('JQUANTS_EMAIL') or '',
            os.getenv('JQUANTS_PASSWORD') or '',
        )

        if refresh_token_fetcher_output.response_code == RESPONSE_OK:
          id_token_fetcher_output: IDTokenFetchOutput = self.id_token_fetcher.fetch(
            refresh_token_fetcher_output.token
          )
        else:
          raise RefreshTokenException(
            refresh_token_fetcher_output.response_code,
            refresh_token_fetcher_output.error_message,
          )
        if id_token_fetcher_output.response_code == RESPONSE_OK:
          self._id_token = id_token_fetcher_output.token
        else:
          raise IDTokenFetcherException(
            id_token_fetcher_output.response_code,
            id_token_fetcher_output.error_message,
          )
        return self._id_token
      else:
        return self._id_token
