from imagetext import ImageText
from act2.gamesetup import GameSetup

class Introduction(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         text="Something is odd, the US closed their border, "
                                        "diseases appear to follow a pattern, "
                                        "but what kind of pattern",
                         image='Pandemic.jpg',
                         **kwargs)

    def next(self):
        return GameSetup(self.main)