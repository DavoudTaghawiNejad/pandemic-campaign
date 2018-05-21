from imagetext import ImageText
from act3.introduction import Introduction


class End(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         image='terrorist.jpg',
                         text="You caught the bio terrorist!")

    def next(self):
        return Introduction(self.main)
