from kivy.uix.label import Label
from act3.gamesetup import GameSetup


class Introduction(Label):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, text="After successfully eliminating the BioTerrorist we need to clean up his mess")
        self.main = main
        self.main.next_visible(True)


    def next(self):
        return GameSetup(self.main)