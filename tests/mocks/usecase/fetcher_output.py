from j_quants_auth import JQuantsApiIDTokenController
from j_quants_auth.usecase import IIDTokenFetcher, IRefreshTokenFetcher
from j_quants_auth.usecase.fetcher_output import BaseTokenFetcherOutput

class MockIDTokenFetcher(IIDTokenFetcher):
    pass


class MockRefreshTokenFetcher(IRefreshTokenFetcher):
    pass

class MockTokenOutput(BaseTokenFetcherOutput):
    def __init__(
        self,
        response_code,
        response_message,
        token,
    ):
        self.response_code = response_code
        self.response_message = response_message
        self.token = token
