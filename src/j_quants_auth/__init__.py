from .controller import JQuantsApiIDTokenController
from .usecase import (
  RefreshTokenFetcher,
  IDTokenFetcher,
)

JQuantsAuthorization = JQuantsApiIDTokenController(
  RefreshTokenFetcher(),
  IDTokenFetcher(),
)

__all__ = ['JQuantsAuthorization']
