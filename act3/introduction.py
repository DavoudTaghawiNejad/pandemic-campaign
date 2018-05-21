from imagetext import ImageText
from act3.gamesetup import GameSetup


class Introduction(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         image='terrorist.jpg',
                         text="After successfully eliminating the bio terrorist we need to clean up his mess.")

    def next(self):
        return GameSetup(self.main)