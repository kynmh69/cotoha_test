from tkinter import Frame, Button

from cotoha_api.cotoha_api import CotohaApi
from logger.logger import LoggerUtils


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.logger = LoggerUtils.get_instance()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        cotoha_api = CotohaApi()
        hi_there = Button(self)
        hi_there["text"] = "DO API \n(click me)"
        sentence = "KDDI株式会社"
        self.logger.info(sentence)
        hi_there["command"] = lambda: cotoha_api.named_entity_extraction(sentence)
        hi_there.pack(side="top")

        quit_ = Button(self, text="QUIT", fg="red",
                       command=self.master.destroy)
        quit_.pack(side="bottom")
