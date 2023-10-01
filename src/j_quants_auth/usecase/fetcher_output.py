from abc import ABC, abstractmethod
import requests
from typing import Optional
from ..constants import RESPONSE_OK

class BaseTokenFetcherOutput(ABC):
    response_code: str
    response_message: str
    token: str

    def __init__(
        self,
        response,
    ):
        response_json = response.json()
        self.response_code = response.status_code 
        if self.response_code == RESPONSE_OK:
            self.token = self._get_token_from_json(response_json)

    @abstractmethod
    def _get_token_from_json(self, response_json: requests.Response) -> Optional[str]:
        pass

class RefreshTokenFetchOutput(BaseTokenFetcherOutput):
    def _get_token_from_json(self, response_json: requests.Response) -> Optional[str]:
        return response_json.get('refreshToken', None)


class IDTokenFetchOutput(BaseTokenFetcherOutput):
    def _get_token_from_json(self, response_json: requests.Response) -> Optional[str]:
        return response_json.get('idToken', None)