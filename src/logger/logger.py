from datetime import datetime
from logging import DEBUG, Formatter, StreamHandler, getLogger, FileHandler, INFO


class LoggerUtils:
    """
    First call def logger_initialize(self).
    and use get_instance.

    """
    __unique_instance = None

    def __init__(self):
        raise NotImplementedError("This class is singleton.")

    @classmethod
    def __internal_new__(cls):
        return getLogger()

    @classmethod
    def get_instance(cls):
        if not cls.__unique_instance:
            cls.__unique_instance = cls.__internal_new__()

        return cls.__unique_instance


def logger_initialize():
    """
    logger initializer
    """
    date_time = datetime.now().strftime("%Y%m%d%H%M")
    file_name = f"./log/{date_time}_cotoha.log"
    logger = getLogger()
    stream_handler = StreamHandler()
    file_handler = FileHandler(file_name)
    formatter = Formatter('%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s')

    stream_handler.setLevel(DEBUG)
    stream_handler.setFormatter(formatter)
    file_handler.setLevel(INFO)
    file_handler.setFormatter(formatter)
    logger.setLevel(DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
