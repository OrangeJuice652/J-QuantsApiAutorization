from abc import ABC, abstractmethod
import requests
import json
from ..constants import JQUANTS_API_URI, REFRESH_TOKEN_URL
from .fetcher_output import RefreshTokenFetchOutput


class IRefreshTokenFetcher(ABC):
    mail_address: str
    password: str

    @abstractmethod
    def __init__(
        self,
        mail_address: str,
        password: str,
    ):
        pass

    @abstractmethod
    def fetch(self) -> RefreshTokenFetchOutput:
        pass

class RefreshTokenFetcher(IRefreshTokenFetcher):
    mail_address: str
    password: str

    def __init__(
        self,
        mail_address: str = '',
        password: str = '',
    ):
        self.mail_address = mail_address
        self.password = password

    def fetch(self) -> RefreshTokenFetchOutput:
        request_body = {
            'mailaddress': self.mail_address,
            'password': self.password,
        }
        response: requests.Response = requests.post(
            JQUANTS_API_URI+REFRESH_TOKEN_URL,
            data=json.dumps(request_body),
        )
        return RefreshTokenFetchOutput(response)