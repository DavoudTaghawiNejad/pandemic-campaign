from imagetext import ImageText
from act2.game import Game
from random import sample


class GameSetup(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         text="Setup:\n"
                              "- Remove all blue cards from the infection deck\n"
                              "\n"
                              "- Set up a CDC in %s and %s" % tuple(sample(main.legacy.cdcs, 2)))

    def next(self):
        return Game(self.main)