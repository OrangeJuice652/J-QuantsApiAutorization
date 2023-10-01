from abc import ABC, abstractmethod


class IAPIResponseException(ABC, Exception):
    api_verbose_name: str
    response_code: str
    response_message: str

    @abstractmethod
    def __init__(self, response_code, response_message):
        pass


class APIResponseException(IAPIResponseException):
    def __init__(self, response_code, response_message):
        self.response_code = response_code
        self.response_message = response_message
    
    def __str__(self):
        f'{self.api_verbose_name}の呼び出しに失敗しました。\
        (response_code: {self.response_code} \
        response_message: {self.response_message})'


class RefreshTokenException(APIResponseException):
    api_verbose_name = 'リフレッシュトークン取得'


class IDTokenFetcherException(APIResponseException):
    api_verbose_name = 'IDトークン取得'

