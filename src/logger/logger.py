from logging import DEBUG, Formatter, StreamHandler, getLogger, Logger


class LoggerUtils():
    """
    First call def logger_initialze(self).
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

def logger_initialze():
    """
    logger initializer
    """
    logger = getLogger()
    handler = StreamHandler()
    formatter = Formatter('%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s')
    handler.setLevel(DEBUG)
    handler.setFormatter(formatter)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
