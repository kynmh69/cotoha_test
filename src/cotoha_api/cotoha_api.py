from configparser import ConfigParser
from typing import Tuple, Any, Dict

from requests import post
from requests import Response

from src.abstract.cotoha_abs import CotohaAbc, get_config
from src.logger.logger import LoggerUtils


class CotohaApi(CotohaAbc):
    def __init__(self, client_id: str = None, client_secret: str = None) -> None:
        """
        class cotoha api.
        :rtype: object
        :param client_id:
        :param client_secret:
        """
        super().__init__()
        self.__url = "https://api.ce-cotoha.com/api/dev"
        self.__access_token_publish_url = "https://api.ce-cotoha.com/v1/oauth/accesstokens"
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__access_token = ""
        self.__logger = LoggerUtils.get_instance()
        if self.__client_id is None:
            self.__client_id, _ = get_config()
        if self.__client_secret is None:
            _, self.__client_secret = get_config()
        self.get_access_token()

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
            "clientId": self.__client_id,
            "clientSecret": self.__client_secret
        }
        response: Response = post(self.__access_token_publish_url, headers=header, json=payload)
        self.__logger.debug(f'Response: {response.json()}')
        self.__access_token = response.json().get('access_token')
        return

    def architecture_analyze_api(self, sentence: str) -> Dict[str, Any]:
        self.__logger.debug(self)
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": f"Bearer {self.__access_token}"
        }
        payload = {
            "sentence": sentence
        }
        response: Response = post(self.__url + '/nlp/v1/parse', headers=header, json=payload)
        self.__logger.debug(f'Response: {response.json()}')

    def __str__(self) -> str:
        s = (f"uri: {self.__url}, "
             f"access token: {self.__access_token}")
        return s
