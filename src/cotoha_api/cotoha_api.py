from configparser import ConfigParser
from typing import Tuple

from requests import post
from requests import Response

from src.logger.logger import LoggerUtils

CONFIG_FILE_PATH = "/Users/Hiroki/Applications/PythonProjects/cotoha_test/src/setting/setting.conf"
CONFIG_KEY = "settings"


class CotohaApi:
    
    def __init__(self, client_id: str = None, client_secret: str = None) -> None:
        """
        class cotoha api.
        :rtype: object
        :param client_id: 
        :param client_secret: 
        """
        self.__url = "https://api.ce-cotoha.com/api/dev/"
        self.__access_token_publish_url = "https://api.ce-cotoha.com/v1/oauth/accesstokens"
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__access_token = ""
        self.logger = LoggerUtils.get_instance()
        if self.__client_id is None:
            self.__client_id, _ = get_config()
        if self.__client_secret is None:
            _, self.__client_secret = get_config()

        self.get_access_token()

    def get_access_token(self):
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
            "Content-Type": "application/json"
        }
        payload = {
            "grantType": "client_credentials",
            "clientId": self.__client_id,
            "clientSecret": self.__client_secret
        }
        response: Response = post(self.__access_token_publish_url, headers=header, json=payload)
        self.logger.debug(f'Response: {response.json()}')
        self.__access_token = response.json().get('access_token')

    def __str__(self):
        s = (
            f"URI: {self.__url}\n"
            f"Access token: {self.__access_token_publish_url}\n"
        )
        return s


def get_config() -> Tuple[str, str]:
    config = ConfigParser()
    config.read(CONFIG_FILE_PATH)

    settings = config[CONFIG_KEY]
    return settings.get('client_id'), settings.get('client_secret')
