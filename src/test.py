from configparser import ConfigParser
from logging import DEBUG, StreamHandler, getLogger, Formatter
from logger.logger import LoggerUtils, logger_initialze
import sys

CONFIG_FILE_PATH = "src/setting/setting.conf"
CONFIG_KEY = "settings"
EQUAL_STR = "=" * 20


if __name__ == "__main__":
    logger_initialze()
    logger = LoggerUtils.get_instance()
    logger.info(f"{EQUAL_STR} START {EQUAL_STR}")
    config = ConfigParser()
    config.read(CONFIG_FILE_PATH)

    settings = config[CONFIG_KEY]
    client_id = settings.get('client_id')
    client_secret = settings.get('client_secret')
    logger.debug(f'client id: {client_id}')
    logger.debug(f'client secret: {client_secret}')

    logger.info(f"{EQUAL_STR} END {EQUAL_STR}")
