import json
from configparser import ConfigParser
from enum import Enum, auto
from typing import Tuple, Any, Dict, List

from requests import post
from requests import Response

from src.abstract.cotoha_abs import CotohaApiAbc, get_config, CotohaResponseAbc
from src.logger.logger import LoggerUtils


class CotohaApiResponse(CotohaResponseAbc):
    def __init__(self, result: List[Dict[str, Any]], status: int, message: str):
        super().__init__(result, status, message)
        return


class RequestBody(Enum):
    """

    """
    default = auto()
    kuzure = auto()


class CotohaApi(CotohaApiAbc):
    def __init__(self, client_id: str = None, client_secret: str = None) -> None:
        """
        class cotoha api.
        :rtype: None
        :param client_id:
        :param client_secret:
        """
        super().__init__(client_id, client_secret)
        self.__logger = LoggerUtils.get_instance()
        self.get_access_token()
        return

    def get_access_token(self) -> None:
        """
        get Access token
        {
            "access_token": "アクセストークン",
            "token_type": "bearer",
            "expires_in": "残り有効期限(秒)" ,
            "scope": "" ,
            "issued_at": "トークン発行日時(エポックタイムからの経過ミリ秒数)"
        }
        """
        header = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        payload = {
            "grantType": "client_credentials",
            "clientId": self.client_id,
            "clientSecret": self.client_secret
        }
        response: Response = post(self.access_token_publish_url, headers=header, json=payload)
        self.__logger.debug(f'Response: {response.json()}')
        self.access_token = response.json().get('access_token')
        return

    def architecture_analyze_api(self, sentence: str, req_body: RequestBody = RequestBody.default.name) \
            -> CotohaApiResponse:
        self.__logger.debug(self)
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": f"Bearer {self.access_token}"
        }
        payload = {
            "sentence": sentence,
            "type": req_body
        }
        response: Response = post(self.uri + '/nlp/v1/parse', headers=header, json=payload)
        self.__logger.info(f'Response: {response.json()}')
        return CotohaApiResponse(response.json().get('result'), response.json().get('status'),
                                 response.json().get('message'))

    def __str__(self) -> str:
        s = (f"uri: {self.uri}, "
             f"access token: {self.access_token}")
        return s
