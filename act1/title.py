from imagetext import ImageText
from act1.introduction import Introduction


class Title(ImageText):
    def __init__(self, main, **kwargs):
        super().__init__(main=main,
                         text="[size=24sp]Welcome to Trumpft the Pandemic the Campaign[/size]",
                         image='Pandemic.jpg',
                         **kwargs)

    def next(self):
        return Introduction(self.main)