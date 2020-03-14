from logging import DEBUG, Formatter, StreamHandler, getLogger, Logger

class LoggerUtils():
    """
    First call def logger_initialze(self).
    and use get_instance.

    """
    __unique_instance = None
    @classmethod
    def get_instance(cls) -> Logger:
        """
        get instance
        """
        return getLogger(__name__)
    @classmethod
    def logger_initialze(cls):
        """
        logger initializer
        """
        logger = cls.get_instance()
        handler = StreamHandler()
        formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)
