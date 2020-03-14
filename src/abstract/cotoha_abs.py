from abc import ABCMeta
from configparser import ConfigParser
from typing import Dict, Any, Tuple

CONFIG_FILE_PATH = "/Users/Hiroki/Applications/PythonProjects/cotoha_test/src/setting/setting.conf"
CONFIG_KEY = "settings"
ENCODING = 'utf-8'


class CotohaAbc(metaclass=ABCMeta):
    __url: str

    def __init__(self, client_id=None, client_secret=None):
        """

        :rtype: None
        """
        self.__url = "https://api.ce-cotoha.com/api/dev"
        self.__access_token_publish_url = "https://api.ce-cotoha.com/v1/oauth/accesstokens"
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__access_token = ""
        if self.client_id is None:
            self.__client_id, _ = get_config()
        if self.__client_secret is None:
            _, self.__client_secret = get_config()
        return

    @property
    def uri(self) -> str:
        return self.__url

    @property
    def access_token_publish_url(self) -> str:
        return self.__access_token_publish_url

    @property
    def client_id(self):
        return self.__client_id

    @property
    def client_secret(self):
        return self.__client_secret

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, access_token):
        self.__access_token = access_token
        return

    def get_access_token(self):
        pass

    def architecture_analyze_api(self, sentence: str) -> Dict[str, Any]:
        pass


def get_config() -> Tuple[str, str]:
    config = ConfigParser()
    config.read(CONFIG_FILE_PATH)

    settings = config[CONFIG_KEY]
    return settings.get('client_id'), settings.get('client_secret')
