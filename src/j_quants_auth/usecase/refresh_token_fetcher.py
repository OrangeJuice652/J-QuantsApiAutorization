from abc import ABC, abstractmethod
import requests
import json
from ..constants import JQUANTS_API_URI, REFRESH_TOKEN_URL
from .fetcher_output import RefreshTokenFetchOutput


class IRefreshTokenFetcher(ABC):
    @abstractmethod
    def fetch(self,
        mail_address: str,
        password: str,
    ) -> RefreshTokenFetchOutput:
        pass

class RefreshTokenFetcher(IRefreshTokenFetcher):
    def fetch(
        self,
        mail_address: str,
        password: str,
    ) -> RefreshTokenFetchOutput:
        request_body = {
            'mailaddress': mail_address,
            'password': password,
        }
        response: requests.Response = requests.post(
            JQUANTS_API_URI+REFRESH_TOKEN_URL,
            data=json.dumps(request_body),
        )
        return RefreshTokenFetchOutput(response)