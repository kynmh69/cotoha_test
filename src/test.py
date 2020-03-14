import json
from configparser import ConfigParser

from src.abstract.cotoha_abs import ENCODING
from src.cotoha_api.cotoha_api import CotohaApi, CotohaApiResponse
from src.logger.logger import logger_initialize, LoggerUtils


EQUAL_STR = "=" * 20

if __name__ == "__main__":
    logger_initialize()
    logger = LoggerUtils.get_instance()
    logger.info(f"{EQUAL_STR} START {EQUAL_STR}")
    cotoha = CotohaApi()
    while True:
        try:
            input_str = input('> ')
            res: CotohaApiResponse = cotoha.architecture_analyze_api(input_str, )
            logger.info(f'status: {res.status}')
            logger.info(f'message: {res.message}')
            for i in res.result:
                print(json.dumps(i, indent=4, ensure_ascii=False))

            res = cotoha.sentiment(input_str)
            logger.info(f'status: {res.status}')
            logger.info(f'message: {res.message}')
            if res.status == 0:
                logger.info(f'{round(res.result.get("score") * 100, 1)}%の確率で、{res.result.get("sentiment")}')

        except KeyboardInterrupt:
            print()
            break

    logger.info(f"{EQUAL_STR} END {EQUAL_STR}")
