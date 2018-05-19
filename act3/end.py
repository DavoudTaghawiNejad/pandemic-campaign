from kivy.uix.label import Label
from act3.gameend import GameEnd



class End(Label):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, text="All diseases cured!")
        main.next_visible(True)
        self.main = main


    def next(self):
        return GameEnd(self.main)