from kivy.uix.label import Label
from act2.gamesetup import GameSetup


class Introduction(Label):
    def __init__(self, main, **kwargs):
        super().__init__(**kwargs, text="Something is odd, the US closed their border, "
                                        "diseases appear to follow a pattern, "
                                        "but what kind of pattern")
        self.main = main


    def next(self):
        return GameSetup(self.main)