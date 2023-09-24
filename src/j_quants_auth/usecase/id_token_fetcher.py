from abc import ABC, abstractmethod
import requests
from typing import Optional
from ..constants import JQUANTS_API_URI, ID_TOKEN_URL
from .fetcher_output import IDTokenFetchOutput

class IIDTokenFetcher(ABC):
    @abstractmethod
    def __init__(
        self,
        refresh_token: Optional[str] = None,
    ):
        pass

    @abstractmethod
    def fetch() -> IDTokenFetchOutput:
        pass


class IDTokenFetcher():
    def __init__(
        self,
        refresh_token: Optional[str] = None,
    ):
        self.refresh_token = refresh_token

    def fetch(self) -> IDTokenFetchOutput:
        query_parameters = {
            'refreshtoken': self.refresh_token,
        }
        response: requests.Response = requests.post(
            JQUANTS_API_URI+ID_TOKEN_URL,
            params=query_parameters,
        )
        return IDTokenFetchOutput(response)