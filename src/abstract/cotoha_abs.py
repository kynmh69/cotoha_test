from abc import ABCMeta
from configparser import ConfigParser
from typing import Dict, Any, Tuple

CONFIG_FILE_PATH = "/Users/Hiroki/Applications/PythonProjects/cotoha_test/src/setting/setting.conf"
CONFIG_KEY = "settings"


class CotohaAbc(metaclass=ABCMeta):

    def get_access_token(self):
        pass

    def architecture_analyze_api(self, sentence: str) -> Dict[str, Any]:
        pass


def get_config() -> Tuple[str, str]:
    config = ConfigParser()
    config.read(CONFIG_FILE_PATH)

    settings = config[CONFIG_KEY]
    return settings.get('client_id'), settings.get('client_secret')
