from imagetext import ImageText
from act1.gamesetup import GameSetup


class Introduction(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         text="[size=24sp]Welcome to Trumpft the Pandemic the Campaign[/size]\n"
                              "The way it works is that you play a regular pandemic game, sometimes\n"
                              "with a special setup. While you are playing the game you let the\n"
                              "campaign up know what you are doing.\n"
                              "As you are playing the story unfolds.\n",
                         image=None,
                         **kwargs)

    def next(self):
        return GameSetup(self.main)