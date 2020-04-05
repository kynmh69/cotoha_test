import json
from tkinter import Tk

from gui.gui import Application
from src.cotoha_api.cotoha_api import CotohaApi, CotohaApiResponse
from src.logger.logger import logger_initialize, LoggerUtils

EQUAL_STR = "=" * 20

if __name__ == "__main__":
    logger_initialize()
    logger = LoggerUtils.get_instance()
    logger.info(f"{EQUAL_STR} START {EQUAL_STR}")
    app = Application()
    app.create_window()
    app.create_sentence_form()
    app.master.mainloop()
    logger.info(f"{EQUAL_STR} END {EQUAL_STR}")
