import requests
from src.j_quants_auth.usecase.fetcher_output import BaseTokenFetcherOutput


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
    
    def _get_token_from_json(self, response_json):
        return None
