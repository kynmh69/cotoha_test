from tkinter import Frame, Button, Entry, Tk, Menubutton
from typing import Union

from cotoha_api.cotoha_api import CotohaApi
from logger.logger import LoggerUtils


class Application:
    def __init__(self, master=None):
        self.__master: Union[None, Tk] = None
        self.__logger = LoggerUtils.get_instance()
        self.__sentence_entry: Union[None, Entry] = None
        self.__result_entry: Union[None, Entry] = None
        self.__submit_button: Union[None, Button] = None
        self.__menu_button: Union[None, Menubutton] = None
        return

    @property
    def master(self):
        """
        Master of Tk().
        :return:
        """
        return self.__master

    def create_window(self) -> None:
        """
        Create window.
        :return:
        """
        self.__master = Tk()
        self.__master.title('Cotoha API')
        self.__master.geometry('1920x1080')
        return

    def create_form(self) -> None:
        """
        Create Form
        :return:
        """
        self.__sentence_entry = Entry(self.__master)
        return
