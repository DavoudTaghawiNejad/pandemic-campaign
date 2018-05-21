from imagetext import ImageText
from act3.gameend import GameEnd


class End(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         image='terrorist.jpg',
                         text="You cured all diseases; survived the Trump administration and"
                              "you caught the bio terrorist!")

    def next(self):
        return GameEnd(self.main)