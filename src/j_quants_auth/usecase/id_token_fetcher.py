from abc import ABC, abstractmethod
import requests
from ..constants import JQUANTS_API_URI, ID_TOKEN_URL
from .fetcher_output import IDTokenFetchOutput

class IIDTokenFetcher(ABC):
    @abstractmethod
    def fetch(self, refresh_token: str) -> IDTokenFetchOutput:
        pass


class IDTokenFetcher():
    def fetch(
        self,
        refresh_token: str,
    ) -> IDTokenFetchOutput:
        query_parameters = {
            'refreshtoken': refresh_token,
        }
        response: requests.Response = requests.post(
            JQUANTS_API_URI+ID_TOKEN_URL,
            params=query_parameters,
        )
        return IDTokenFetchOutput(response)
