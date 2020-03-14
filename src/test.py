from configparser import ConfigParser
from logging import DEBUG, StreamHandler, getLogger, Formatter
from src.logger.logger import LoggerUtils


CONFIG_FILE_PATH = "src/setting/setting.conf"
CONFIG_KEY = "settings"
EQUAL_STR = "=" * 20



if __name__ == "__main__":
    LoggerUtils.logger_initialze()
    logger = LoggerUtils.get_instance()
    logger.info(f"{EQUAL_STR} START {EQUAL_STR}")
    config =  ConfigParser()
    config.read(CONFIG_FILE_PATH)

    settings = config[CONFIG_KEY]
    
    logger.info(f"{EQUAL_STR} END {EQUAL_STR}")
