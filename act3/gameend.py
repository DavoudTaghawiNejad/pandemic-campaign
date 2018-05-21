from imagetext import ImageText


class GameEnd(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         image='terrorist.jpg',
                         text="You cured all diseases; survived the Trump administration and"
                              "you caught the bio terrorist!")