from tkinter import Button, Entry, Tk, Menubutton, Label, TOP, BOTTOM
from typing import Union

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

    def create_sentence_form(self) -> None:
        """
        Create Form
        :return:
        """
        label = Label(self.__master, text='Sentence')
        label.pack(side=TOP)
        self.__sentence_entry = Entry(self.__master, bd=2)
        self.__sentence_entry.pack(BOTTOM)
        return
