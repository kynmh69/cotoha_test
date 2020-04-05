from configparser import ConfigParser
from pathlib import Path
from tkinter import Button, Entry, Tk, Menubutton, Label, TOP, BOTTOM, RAISED, Menu, IntVar
from typing import Union

from cotoha_api.cotoha_api import CotohaApi
from logger.logger import LoggerUtils


class Application:
    def __init__(self):
        self.__master: Union[None, Tk] = None
        self.__logger = LoggerUtils.get_instance()
        self.__sentence_entry: Union[None, Entry] = None
        self.__result_entry: Union[None, Entry] = None
        self.__submit_button: Union[None, Button] = None
        self.__menu_button: Union[None, Menubutton] = None
        self.__vertical_px = 1080
        self.__horizontal_px = 1920
        self.__window_title = 'Cotoha API'
        self.__setting = ConfigParser()
        self.__cotoha_api = CotohaApi()
        return

    @property
    def master(self):
        """
        Master of Tk().
        :return:
        """
        return self.__master

    @property
    def vertical_px(self):
        """

        :return:
        """
        return self.__vertical_px

    @property
    def horizontal_px(self):
        """

        :return:
        """
        return self.__horizontal_px

    @property
    def window_title(self):
        """

        :return:
        """
        return self.__window_title

    def create_window(self) -> None:
        """
        Create window.
        :return:
        """
        self.__master = Tk()
        self.__master.title(self.window_title)
        self.__master.geometry(f'{self.horizontal_px}x{self.vertical_px}')
        return

    def create_sentence_form(self) -> None:
        """
        Create Form
        :return:
        """
        label = Label(self.__master, text='Sentence')
        label.pack(side=TOP)
        self.__sentence_entry = Entry(self.__master, bd=2)
        self.__sentence_entry.pack(side=BOTTOM)
        return

    def create_pull_down_menu(self):
        mb = Menubutton(self.master, text='Select API.', relief=RAISED)
        mb.grid()
        mb.menu = Menu(mb, tearoff=0)
        mb['menu'] = mb.menu
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()

        mb.menu.add_checkbutton(label="")
        return

    def read_config(self):
        path = Path('src/setting/setting.conf')
        if path.exists():
            raise FileExistsError

        self.__setting.read(path)

        return
