from configparser import ConfigParser

from src.cotoha_api.cotoha_api import CotohaApi, get_config
from src.logger.logger import logger_initialze, LoggerUtils


EQUAL_STR = "=" * 20

if __name__ == "__main__":
    logger_initialze()
    logger = LoggerUtils.get_instance()
    logger.info(f"{EQUAL_STR} START {EQUAL_STR}")

    cotoha = CotohaApi()
    logger.info(f"{EQUAL_STR} END {EQUAL_STR}")
